#!/usr/bin/env ruby
x = ARGV[0]
def function(x)
    puts x.scan(/\[from:.+\]\s\[to:.+\]\s\[flags:.+-1\]/).join
end

 function(x)