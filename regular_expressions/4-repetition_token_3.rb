#!/usr/bin/env ruby
x = ARGV[0]
def function(x)
    x.scan(/hbt{0,4}n/).join
end

function(x)