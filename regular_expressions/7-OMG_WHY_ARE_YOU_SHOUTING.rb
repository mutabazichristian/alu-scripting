#!/usr/bin/env ruby
x = ARGV[0]
def function(x)
    puts x.scan(/^[A-Z]*$/)
end

function(x)