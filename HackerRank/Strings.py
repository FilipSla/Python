def split_and_join(line):
   """
   #1. možnost
   line = line.split(" ")
   line = "-".join(line)

   #2. možnost
   line = line.replace(" ","-")
   """
   #3. možnost
   line = "-".join(line.split())
   return line
randomVeta = "Dnes je venku krásné počasí"
transformedSentece = split_and_join(randomVeta)
print(transformedSentece)
