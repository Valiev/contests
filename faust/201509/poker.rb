SOURCE = File.expand_path "~/Downloads/Data"
DESTINATION = File.expand_path "~/Poker"

require 'zip'
require 'date'
require 'shellwords'

CURRENT_YEAR = Date.today.year
YEARS = 2010.upto(CURRENT_YEAR).to_a

LIMITS = {
  "3-6"      => '-3-6-',
  "4-8"      => '-4-8-',
  "5-10"      => '-5-10-',
  "7.50-15"   => '-7.50-15-',
  "8-16"      => '-8-16-',
  "10-10"     => '-10-10-',
  "10-20"     => '-10-20-',
  "15-30"     => '-15-30-',
  "20-20"     => '-20-20-',
  "20-40"     => '-20-40-',
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
    "PokerStars-FixedLimitHoldem",
    "FixedLimitHoldem-Stars"
  ],

  "FL Holdem-PartyPoker" => [
    "FixedLimitHoldem-PartyPoker"
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

  "PL Omaha-IPoker" => [
    "PotLimitOmaha-IPoker"
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
    "Pacific-NoLimitHoldem",
    "NL Holdem-Pacific"
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

  "FL Holdem-IPoker" => [
    "FixedLimitHoldem-IPoker",
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
    # -$5-$10- pattern
    dollar_pattern = limit_pattern.gsub(/\d+/) {|s| "\\$#{s}"}
    YEARS.each do |year|
      patterns = [
        # Finsen II CAP,20-50 bb-5-10-Cap NL Holdem-PokerStars-1-15-2014.txt
        # Aglasun 817033778-20-40-EURO-FixedLimitHoldem-IPoker-1-16-2014.txt
        # Posadas (Real Money)-50-100-NL Holdem-Pacific-5-18-2012.txt
        %r|.*(?<gameinfo>.*)(?<limit>#{limit_pattern})(?<spam>.*)#{poker_pattern}(?<date_info>.*)(?<year>-#{year}).*|,
        %r|.*(?<gameinfo>.*)(?<limit>#{dollar_pattern})(?<spam>.*)#{poker_pattern}(?<date_info>.*)(?<year>-#{year}).*|,
        %r|.*(?<gameinfo>.*)(?<limit>#{limit_pattern})#{poker_pattern}(?<date_info>.*)(?<year>-#{year}).*|,
        %r|.*(?<gameinfo>.*)(?<limit>#{limit_pattern})USD-#{poker_pattern}(?<date_info>.*)(?<year>-#{year}).*|,
        %r|.*(?<gameinfo>.*)(?<limit>#{limit_pattern})EURO-#{poker_pattern}(?<date_info>.*)(?<year>-#{year}).*|,
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
    return rename2 source_file, dest_file
  end

  names = names_with_suffix dest_file
  is_unique = names.select do |n|
    File.exists?(n) && FileUtils.cmp(n, source_file)
  end.empty?

  if is_unique
    uniq_name = names.last
    log2 "Synonym found, copying to #{uniq_name}"
    mkdir dest_folder
    rename2 source_file, uniq_name
  else
    log2 "Duplicate found, removing #{File.basename source_file}"
    remove2 source_file
  end
end

def remove2 path
  remove path
  log_delete
end

def rename2 src, dest
  rename src, dest
  log_move
end

def show_stats
  log2 "=" * 80
  log2 "STATS:"
  log2 "#{STATS[:moved]} file(s) moved"
  log2 "#{STATS[:deleted]} file(s) removed"
end

def process_file path
  match = parse_by_name path

  if match.nil?
    destination = File.join(DESTINATION, 'other')
  else
    destination = File.join(DESTINATION, match[:poker], match[:limit], match[:year].to_s)
  end
  kind_move path, destination
end

def is_empty_tree folder
  entries = (Dir.entries(folder) - %w(. .. .DS_Store ._.DS_Store))
  subfolders = []
  entries.each do |entry|
    e = File.join folder, entry
    if File.directory? e
      subfolders << e
    else
      return false
    end
  end

  subfolders.each do |subfolder|
    return false unless is_empty_tree(subfolder)
  end
  return true
end

def process_zip_file path
  Dir.mktmpdir 'poker_' do |tempdir|
    Zip::File.open(path) do |ziphandle|
      total = ziphandle.entries.length
      name = File.basename path
      ziphandle.each_with_index do |zipped_file, idx|
        log2 "[#{idx}/#{total}] processing #{name}"
        filename = File.basename zipped_file.name
        next if filename.end_with? '/'
        next if filename.end_with? '.icloud'
        next if filename.include? '.DS_Store'
        output_file = File.join tempdir, filename
        zipped_file.extract output_file
        # Do not process if it's directory
        next if Dir.exists? output_file
        ext = File.extname output_file

        if ['.txt', '.dat'].include? ext
          process_file output_file
        elsif ext == '.zip'
          process_zip_file output_file
        else
          raise "Enable to process #{output_file}"
        end

      end
    end
    remove2 path
  end
end

Maid.rules do
  rule "Process TXT files" do

    dir("#{SOURCE}/**/*.txt").each do |path|
      process_file path
    end

  end

  rule "Process DAT files" do

    dir("#{SOURCE}/**/*.dat").each do |path|
      process_file path
    end

  end

  rule "Process ZIP files" do

    dir("#{SOURCE}/**/*.zip").each do |path|
      log2 "processing zip #{path}"
      process_zip_file path
    end

  end

  rule "Delete .cloud files" do
    dir("#{SOURCE}/**/.*").each do |path|
      ext = File.extname path
      remove2 path if ext == '.icloud'
    end

  end

  rule "Delete Empty folders" do
    dir("#{SOURCE}/**/*/").each do |folder|
      next unless Dir.exist? folder
      remove2 folder if is_empty_tree folder
    end
  end

  rule "Show stats" do

    show_stats

  end
end
