require 'rubygems'
require 'bundler'
Bundler.require
require 'linguist'
require 'json'

def getFileInfo(f)
  filename = f.chomp
  fblob = Linguist::FileBlob.new(filename)
  info = { "filename" => filename }
  begin
    lang = fblob.language
  rescue ArgumentError
    lang = nil
  end
  begin
    info["vendored"] = fblob.vendored?
  rescue ArgumentError
  end
  begin
    info["generated"] = fblob.generated?
  rescue ArgumentError
  end
  if not lang.nil?
    info["language"] = lang.name
    begin
      info["sloc"] = fblob.sloc
    rescue ArgumentError
    end
    begin
      info["loc"] = fblob.loc
    rescue ArgumentError
    end
  end
  info
end

flisttext = File.open(ARGV[0]).read
fout = File.open(ARGV[1], "w")
fparsed = JSON.parse(flisttext)
fout.write(fparsed.collect{|f| getFileInfo(f)}.to_json)
