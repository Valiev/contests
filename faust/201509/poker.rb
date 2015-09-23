SOURCE = "~/Downloads/process_poker"
DESTINATION = "~/Poker"

require 'date'
CURRENT_YEAR = Date.today.year
YEARS = 2001.upto(CURRENT_YEAR).to_a

LIMITS = {
  "5-10"      => '-5-10-',
  "10-20"     => '-10-20-',
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
}

POKER_MAPPING = {
  "FL Holdem-OnGame" => [
    "FL Holdem-OnGame",
    "FixedLimitHoldem-OnGame"
  ],

  "NL Holdem-OnGame" => [
    "NoLimitHoldem-OnGame",
    "NL Holdem-OnGame"
  ],

  "NL Holdem-FullTilt" => [
    "NoLimitHoldem-FullTilt"
  ],

  "NL Holdem-Pacific" => [
    "NoLimitHoldem-Pacific"
  ],

  "FL Holdem-Pacific" => [
    "FixedLimitHoldem-Pacific"
  ],

  "FL Holdem-PokerStars" => [
    "FL Holdem-PokerStars",
    "FixedLimitHoldem-PokerStars"
  ],

  "NL Holdem-PokerStars" => [
    "NL Holdem-PokerStars",
    "NoLimitHoldem-PokerStars"
  ],

  "PL Omaha-PokerStars" => [
    "PLO-PokerStars",
    "PotLimitOmaha-PokerStars"
  ],

  "FL Omaha Hi-Lo-PokerStars" => [
    "FixedLimitOmahaHiLo-PokerStars",
    "FL Omaha Hi-Lo-PokerStars",
    "PokerStars-FixedLimitOmahaHiLo"
  ],

  "PL Omaha-OnGame" => [
    "PotLimitOmaha-OnGame"
  ],

  "PL Omaha Pacific" => [
    "PotLimitOmaha-Pacific"
  ],

  "FL Holdem-FullTilt" => [
    "FixedLimitHoldem-FullTilt"
  ],

  "PL Omaha-FullTilt" => [
    "PotLimitOmaha-FullTilt"
  ],

  "NL Holdem-MicroGaming" => [
    "NoLimitHoldem-MicroGaming"
  ],

  "FL Holdem-MicroGaming" => [
    "FixedLimitHoldem-MicroGaming"
  ],

  "PL Omaha-MicroGaming" => [
    "PotLimitOmaha-MicroGaming"
  ],

  "PL Holdem-PokerStars" => [
    "PotLimitHoldem-PokerStars"
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

def detect_year filepath
  found_years = YEARS.select do |year|
    filepath.include? year.to_s
  end

  case found_years.length
  when 0
    raise "No years found"
  when 1
    return found_years.first.to_s
  else
    raise "Found multiple years"
  end
end

Maid.rules do
  poker_pattern_limit.each do |poker, poker_pattern, limit|
    rule "Poker #{poker_pattern} with limit #{limit}" do
      limit_pattern = LIMITS[limit]

      # Process txt files
      txt_pattern = "*#{poker_pattern}*.txt"
      dir("#{SOURCE}/**/#{txt_pattern}").each do |path|
        # skip pathes without limit pattern
        next unless path.include?(limit_pattern)
        log("Found txt-file #{path} to operate")
        year = detect_year path
        destination = File.join(DESTINATION, poker, limit, year)
        move(path, mkdir(destination))
      end

      # Process zip files
      # zip_pattern = "*#{poker_pattern}*.zip"
      # dir("#{SOURCE}/**/#{zip_pattern}").each do |path|
      #   # skip pathes without limit pattern
      #   next unless path.include?(limit_pattern)
      #   log("Found zip-file #{path} to operate")
      #   year = detect_year path
      #   destination = File.join(DESTINATION, poker, limit, year)
      #   mkdir(destination)
      #   zipfile_contents(path).each do |name|
      #     content = get_content_from_zip path, name
      #     filepath = File.join destination, name
      #     IO.write filepath, content
      #   end
      #   trash(path)
      # end

    end
  end
end