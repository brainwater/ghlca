require 'rubygems'
require 'bundler'
Bundler.require
require 'linguist'
require 'json'

def getFileInfo(f)
  fblob = Linguist::FileBlob.new(f.chomp)
  language = fblob.language.nil? ? "None" : fblob.language.name
  info = { "language" => language, "sloc" => fblob.sloc, "loc" => fblob.loc, "vendored" => fblob.vendored?, "generated" => fblob.generated? }
end

flisttext = File.open(ARGV[0]).read
fout = File.open(ARGV[1], "w")
fout.write(flisttext.each_line.collect{|f| getFileInfo(f)}.to_json)
