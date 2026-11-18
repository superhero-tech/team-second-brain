# frozen_string_literal: true

require 'minitest/autorun'
require 'tmpdir'
require 'fileutils'
require 'open3'
require 'rbconfig'
require 'yaml'

class KnowledgeCheckTest < Minitest::Test
  TEMPLATE = File.expand_path('..', __dir__)

  def setup
    @root = Dir.mktmpdir('team-brain-check-')
    %w[scripts .claude].each do |name|
      FileUtils.cp_r(File.join(TEMPLATE, name), @root, preserve: true)
    end
    # These tests exercise the checker independently of a team's actual content.
    FileUtils.mkdir_p(File.join(@root, '.agents/skills'))
    %w[team-init team-connect team-query team-update team-garden].each do |name|
      source = File.join(TEMPLATE, '.agents/skills', name, 'SKILL.md')
      assert File.file?(source), "Missing shipped skill: #{name}"
      write(".agents/skills/#{name}/SKILL.md", "# Skill fixture\n")
    end
    write('01-Team/team.md', "---\nworking_language: en\n---\n# Team\n")
    write('01-Team/owners.md', "---\nsteward: null\nareas:\n  research:\n    owner: null\n    backup: null\n---\n# Ownership\n")
    write('02-Knowledge/index.md', "# Knowledge\n")
    write('03-Projects/index.md', "# Projects\n")
  end

  def teardown
    FileUtils.remove_entry(@root)
  end

  def write(path, content)
    target = File.join(@root, path)
    FileUtils.mkdir_p(File.dirname(target))
    File.write(target, content)
  end

  def configure
    write('01-Team/team.md', "---\nworking_language: pl\n---\n# Test team\n")
    data = { 'steward' => 'alice', 'areas' => { 'research' => { 'owner' => 'alice', 'backup' => 'bob' } } }
    write('01-Team/owners.md', "#{data.to_yaml}---\n# Ownership\n")
    write('04-Sources/interview.md', "# Interview\nSynthetic test evidence.\n")
  end

  def page(path = '02-Knowledge/customers/finding.md', overrides = {}, body = 'A scoped finding.')
    data = { 'id' => 'customer-finding', 'type' => 'knowledge', 'area' => 'research',
             'status' => 'needs_review', 'reviewed_at' => nil,
             'sources' => [{ 'access' => 'team', 'ref' => '../../04-Sources/interview.md' }] }.merge(overrides)
    write(path, "#{data.to_yaml}---\n# Finding\n\n#{body}\n")
    index = path.split('/').first + '/index.md'
    File.open(File.join(@root, index), 'a') { |file| file.puts "\n- [Finding](#{path.split('/')[1..].join('/')})" }
  end

  def check
    output, status = Open3.capture2e(RbConfig.ruby, File.join(@root, 'scripts/check.rb'))
    [status.success?, output]
  end

  def test_empty_template_and_claude_symlinks
    ok, output = check
    assert ok, output
    assert_includes output, '0 pages, 0 errors, 0 warnings.'
    %w[team-init team-connect team-query team-update team-garden].each do |name|
      link = File.join(@root, '.claude/skills', name)
      assert File.symlink?(link), name
      assert File.file?(File.join(link, 'SKILL.md')), name
    end
  end

  def test_sourced_knowledge_and_nested_project_pass_in_new_layout
    configure
    page
    page('03-Projects/pilot/brief.md', { 'id' => 'pilot-brief', 'type' => 'project' })
    ok, output = check
    assert ok, output
    assert_includes output, '2 pages, 0 errors, 0 warnings.'
  end

  def test_missing_index_entry_is_rejected
    configure
    page
    write('02-Knowledge/index.md', "# Knowledge\n")
    ok, output = check
    refute ok
    assert_includes output, 'expected one index entry'
  end

  def test_source_path_must_exist_after_migration
    configure
    page('02-Knowledge/customers/finding.md', 'sources' => [{ 'access' => 'team', 'ref' => '../../04-Sources/missing.md' }])
    ok, output = check
    refute ok
    assert_includes output, 'shared source file not found'
  end

  def test_source_symlink_cannot_escape_repository
    configure
    external = File.join(File.dirname(@root), File.basename(@root) + '-private.md')
    File.write(external, 'private fixture')
    File.symlink(external, File.join(@root, '04-Sources/private.md'))
    page('02-Knowledge/customers/finding.md', 'sources' => [{ 'access' => 'restricted', 'ref' => '../../04-Sources/private.md' }])
    ok, output = check
    refute ok
    assert_includes output, 'shared source file not found'
  ensure
    FileUtils.rm_f(external) if external
  end

  def test_active_page_requires_distinct_owner_and_backup
    configure
    path = File.join(@root, '01-Team/owners.md')
    File.write(path, File.read(path).sub('backup: bob', 'backup: alice'))
    page('02-Knowledge/customers/finding.md', 'status' => 'active', 'reviewed_at' => '2026-11-18')
    ok, output = check
    refute ok
    assert_includes output, 'requires an owner and a different backup'
  end

  def test_unreviewed_page_does_not_require_an_invented_review_date
    configure
    page
    ok, output = check
    assert ok, output
    page('02-Knowledge/domain/invalid.md', 'id' => 'invalid-review', 'status' => 'active')
    ok, output = check
    refute ok
    assert_includes output, 'invalid reviewed_at'
  end

  def test_historical_page_links_to_valid_successor
    configure
    page
    page('02-Knowledge/customers/old.md',
         { 'id' => 'old-finding', 'status' => 'superseded', 'reviewed_at' => '2026-11-18', 'superseded_by' => 'customer-finding' },
         'See [current finding](finding.md).')
    ok, output = check
    assert ok, output
    path = File.join(@root, '02-Knowledge/customers/old.md')
    File.write(path, File.read(path).sub('[current finding](finding.md)', 'current finding'))
    ok, output = check
    refute ok
    assert_includes output, 'missing successor link'
  end

  def test_missing_working_language_is_rejected
    write('01-Team/team.md', "---\nworking_language: null\n---\n# Team\n")
    ok, output = check
    refute ok
    assert_includes output, 'working_language must be a non-empty language code or name'
  end

  def test_duplicate_ids_and_broken_links_are_rejected
    configure
    page
    page('02-Knowledge/customers/duplicate.md', {}, '[Source](missing.md)')
    ok, output = check
    refute ok
    assert_includes output, 'also appears in'
    assert_includes output, 'broken link missing.md'
  end
end
