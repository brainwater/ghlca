require 'rubygems'
require 'bundler'
Bundler.require
require 'linguist'
require 'json'

def getFileInfo(f)
  fblob = Linguist::FileBlob.new(f.chomp)
  info = {}
  lang = fblob.language
  if lang.nil?
    info = { "filename" => f.chomp, "vendored" => fblob.vendored?, "generated" => fblob.generated? }
  else
    info = { "filename" => f.chomp, "language" => lang.name, "sloc" => fblob.sloc, "loc" => fblob.loc, "vendored" => fblob.vendored?, "generated" => fblob.generated? }
  end
  info
end

flisttext = File.open(ARGV[0]).read
fout = File.open(ARGV[1], "w")
fparsed = JSON.parse(flisttext)
fout.write(fparsed.collect{|f| getFileInfo(f)}.to_json)
