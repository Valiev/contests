SOURCE = File.expand_path "~/Downloads/Data"
DESTINATION = File.expand_path "~/Poker"

require 'zip'
require 'date'
require 'shellwords'

CURRENT_YEAR = Date.today.year
YEARS = 2010.upto(CURRENT_YEAR).to_a

LIMITS = {
  "5-10"      => '-5-10-',
  "10-20"     => '-10-20-',
  "7.50-15"   => '-7.50-15-',
  "8-16"      => '-8-16-',
  "10-10"     => '-10-10-',
  "15-30"     => '-15-30-',
  "25-50"     => '-25-50-',
  "30-60"     => '-30-60-',
  "50-100"    => '-50-100-',
  "75-150"    => '-75-150-',
  "100-200"   => '-100-200-',
  "200-400"   => '-200-400-',
  "250-500"   => '-250-500-',
  "300-600"   => '-300-600-',
  "400-800"   => '-400-800-',
  "500-1000"  => '-500-1,000-',
  "1000-2000" => '-1,000-2,000-',
  "2000-4000" => '-2,000-4,000-'
}

POKER_MAPPING = {
  "NL Holdem-PokerStars" => [
    "NL Holdem-PokerStars",
    "NoLimitHoldem-PokerStars",
    "PokerStars-NoLimitHoldem"
  ],

  "FL Holdem-PokerStars" => [
    "FL Holdem-PokerStars",
    "FixedLimitHoldem-PokerStars",
    "PokerStars-FixedLimitHoldem"
  ],

  "PL Omaha-FullTilt" => [
    "PotLimitOmaha-FullTilt",
    "FullTilt-PotLimitOmaha"
  ],

  "PL Omaha-Pacific" => [
    "PotLimitOmaha-Pacific",
    "Pacific-PotLimitOmaha"
  ],

  "PL Omaha-PokerStars" => [
    "PLO-PokerStars",
    "PotLimitOmaha-PokerStars",
    "PokerStars-PotLimitOmaha"
  ],

  "PL Omaha-MicroGaming" => [
    "MicroGaming-PotLimitOmaha",
    "PotLimitOmaha-MicroGaming"
  ],

  "PL Omaha-OnGame" => [
    "PotLimitOmaha-OnGame",
    "OnGame-PotLimitOmaha"
  ],

  "FL Holdem-OnGame" => [
    "FL Holdem-OnGame",
    "FixedLimitHoldem-OnGame",
    "OnGame-FixedLimitHoldem"
  ],

  "NL Holdem-OnGame" => [
    "NoLimitHoldem-OnGame",
    "NL Holdem-OnGame",
    "OnGame-NoLimitHoldem"
  ],

  "NL Holdem-FullTilt" => [
    "NoLimitHoldem-FullTilt",
    "FullTilt-NoLimitHoldem"
  ],

  "NL Holdem-Pacific" => [
    "NoLimitHoldem-Pacific",
    "Pacific-NoLimitHoldem"
  ],

  "FL Holdem-Pacific" => [
    "FixedLimitHoldem-Pacific",
    "Pacific-FixedLimitHoldem"
  ],

  "FL Omaha Hi-Lo-PokerStars" => [
    "FixedLimitOmahaHiLo-PokerStars",
    "FL Omaha Hi-Lo-PokerStars",
    "PokerStars-FixedLimitOmahaHiLo"
  ],

  "FL Holdem-FullTilt" => [
    "FixedLimitHoldem-FullTilt",
    "FullTilt-FixedLimitHoldem"
  ],

  "NL Holdem-MicroGaming" => [
    "NoLimitHoldem-MicroGaming",
    "MicroGaming-NoLimitHoldem"
  ],

  "NL Holdem-IPoker" => [
    "NoLimitHoldem-IPoker",
  ],

  "FL Holdem-MicroGaming" => [
    "FixedLimitHoldem-MicroGaming",
    "MicroGaming-FixedLimitHoldem"
  ],

  "PL Holdem-PokerStars" => [
    "PotLimitHoldem-PokerStars",
    "Pot Limit Holdem-PokerStars",
    "PokerStars-PotLimitHoldem"
  ]
}

def poker_pattern_limit
  acc = []
  POKER_MAPPING.each do |type, patterns|
    patterns.each do |pattern|
      LIMITS.each_key do |limit|
        acc << [type, pattern, limit]
      end
    end
  end
  return acc
end

def get_content_from_zip zipped_file, name
  require 'zip'
  Zip::File.open zipped_file do |zipfile|
    entry = zipfile.entries.select {|e| e.name == name}.first
    entry.get_input_stream.read
  end
end

def poker_regexps
  acc = {}
  poker_pattern_limit.each do |poker, poker_pattern, limit|
    limit_pattern = LIMITS[limit]
    YEARS.each do |year|
      patterns = [
        %r|.*(?<gameinfo>.*)(?<limit>#{limit_pattern})EURO-#{poker_pattern}(?<date_info>.*)(?<year>-#{year}).*|,
        %r|.*(?<gameinfo>.*)(?<limit>#{limit_pattern})USD-#{poker_pattern}(?<date_info>.*)(?<year>-#{year}).*|,
        %r|.*(?<gameinfo>.*)(?<limit>#{limit_pattern})#{poker_pattern}(?<date_info>.*)(?<year>-#{year}).*|,
      ].each do |pattern|
        acc[pattern] = {
          :poker => poker,
          :limit => limit,
          :year => year
        }
      end
    end
  end
  return acc
end

POKER_REGEXPS = poker_regexps()

def parse_by_name filepath
  filename = File.basename filepath
  log2 "processing #{filename}"
  POKER_REGEXPS.each do |pattern, data|
    match = pattern.match filepath
    next if match.nil?
    return data
  end

  return nil
end

def names_with_suffix filepath
  ext = File.extname filepath
  name = File.basename filepath, ext
  path = File.dirname filepath

  suffix = 0
  suffix_name = nil
  acc = [filepath]
  while true
    suffix += 1
    suffix_name = File.join(path, "#{name}_#{suffix}#{ext}")
    acc << suffix_name
    break unless File.exists? suffix_name
  end
  acc
end

def log2 msg
  log msg
  $stderr.puts msg
end

def empty_dir? folder
  f = Shellwords.escape folder
  Dir.glob("#{f}/*").empty?
end

STATS = {
  moved: 0,
  deleted: 0
}

def log_move
  STATS[:moved] += 1
end

def log_delete
  STATS[:deleted] +=1
end

def kind_move source_file, dest_folder
  require 'fileutils'

  dest_folder = File.expand_path dest_folder
  basename = File.basename source_file

  dest_file = File.join dest_folder, basename

  unless File.exists? dest_file
    mkdir dest_folder
    return rename(source_file, dest_file)
  end

  names = names_with_suffix dest_file
  is_unique = names.select do |n|
    File.exists?(n) && FileUtils.cmp(n, source_file)
  end.empty?

  if is_unique
    uniq_name = names.last
    log2 "Synonym found, copying to #{uniq_name}"
    mkdir dest_folder
    rename source_file, uniq_name
  else
    log2 "Duplicate found, removing #{source_file}"
    remove(source_file)
  end
end


Maid.rules do
  # rule "Remove empty folders" do
  #   dirs = Dir.glob("#{SOURCE}/**/")
  #   dirs.delete "#{SOURCE}/"

  #   dirs.each do |folder|
  #     remove(folder) if empty_dir? folder
  #   end
  # end

  rule "Find txt files" do
    dir("#{SOURCE}/**/*.txt").each do |path|
      match = parse_by_name path
      raise "Unable to manipulate with file: #{path}" if match.nil?
      destination = File.join(DESTINATION, match[:poker], match[:limit], match[:year].to_s)
      kind_move path, destination
    end
  end

  #poker_pattern_limit.each do |poker, poker_pattern, limit|
  #  limit_pattern = LIMITS[limit]

  #  rule "[TXT] #{poker_pattern} - limit #{limit}" do

  #    # Process txt files
  #    txt_pattern = "*#{poker_pattern}*.txt"
  #    dir("#{SOURCE}/**/#{txt_pattern}").each do |path|
  #      # skip pathes without limit pattern
  #      next unless path.include?(limit_pattern)
  #      year = detect_year path
  #      destination = File.join(DESTINATION, poker, limit, year)
  #      kind_move path, destination
  #    end
  #  end

  #  rule "[DAT] #{poker_pattern} - limit #{limit}" do
  #    dat_pattern = "*#{poker_pattern}*.dat"
  #    dir("#{SOURCE}/**/#{dat_pattern}").each do |path|
  #      # skip pathes without limit pattern
  #      next unless path.include?(limit_pattern)
  #      year = detect_year path
  #      destination = File.join(DESTINATION, poker, limit, year)
  #      kind_move path, destination
  #    end
  #  end

  #  rule "[ZIP] #{poker_pattern} - limit #{limit}" do

  #    zip_pattern = "*#{poker_pattern}*.zip"
  #    dir("#{SOURCE}/**/#{zip_pattern}").each do |path|
  #      # skip pathes without limit pattern
  #      next unless path.include?(limit_pattern)
  #      log2("Found zip-file #{path} to operate")
  #      year = detect_year path
  #      destination = File.join(DESTINATION, poker, limit, year)
  #      mkdir(destination)

  #      # Create temp directory and extract zip
  #      # contents there
  #      Dir.mktmpdir 'poker_' do |tempdir|
  #        Zip::File.open(path) do |zipfile|
  #          zipfile.each do |file|
  #            filename = file.name
  #            file.extract(File.join tempdir, filename)
  #          end
  #        end
  #        # Walk through extracted files and process them
  #        Dir.entries(tempdir).select{ |n|
  #          !File.directory? (File.join(tempdir, n))
  #        }.each do |file|
  #          new_path = File.join(tempdir, file)
  #          log2 "processing from zip #{new_path}"
  #          kind_move new_path, destination
  #        end
  #      end
  #      # We can remove zip file once it was processed
  #      remove path
  #    end
  #  end
  #end

  # rule "Walk through rest of zip files" do
  #   dir("#{SOURCE}/**/*.zip").each do |path|

  #     # Create temp directory and extract zip
  #     # contents there
  #     # FIXME: extract, mig
  #     Dir.mktmpdir 'poker_' do |tempdir|
  #       Zip::File.open(path) do |zipfile|
  #         zipfile.each do |file|
  #           # Skip internal folders
  #           filename = file.name
  #           log2(filename)
  #           next if filename.end_with? '/'
  #           # Skip DS_Store
  #           next if filename.include? '.DS_Store'
  #           extracted_name = File.join tempdir, filename
  #           file.extract extracted_name

  #           p, l, y = recognize_poker_limit_year(extracted_name)
  #           # destination = File.join(DESTINATION, p, l, y)
  #           # kind_move extracted_name, destination
  #         end
  #       end
  #     end
  #     # remove path
  #   end
  # end
end
