#!/usr/bin/env ruby
x = ARGV[0]
def function(x)
    puts x.scan(/hbt{2,5}n/).join
end

function(x)
