#!/usr/bin/env ruby
x = ARGV[0]
def function(x)
    puts x.scan(/\[from:(.+)\]\s\[to:(.+)\]\s\[flags:(.+)\]/).join
end

 function(x)