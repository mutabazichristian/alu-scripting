#!/usr/bin/env ruby
x = ARGV[0]
def function(x)
    puts x.scan(/^\d{10,10}$/).join
end

function(x)