#!/usr/bin/env ruby
x = ARGV[0]
def function(x)
    puts x.scan(/hb?tn/).join
end

function(x)
