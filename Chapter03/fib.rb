if  __FILE__ == $0
  limit = Integer(ARGV[0])
  a = 0
  b = 1
  puts a
  while b < limit
    puts b
    b = a + b
    a = b - a
  end
end
