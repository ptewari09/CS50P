def convert(mood):
    #if mood == ':)'
     #happy=mood.replace(":)","🙂")
     #return happy
    #else
      #sad=mood.replace(":(","🙁")
      #return sad
      mood=mood.replace(":)","🙂").replace(":(","🙁")
      return mood

def main():
   mood=input()
   print(convert(mood))


main()



