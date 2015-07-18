import os
import eyed3

f = open("MusicFiles1.txt", "a")
for root, dirs, files in os.walk("/home/khalil/Music/"):
    for file in files:
        if file.endswith(".mp3"):
            # load id3 tag object into variable
            mfile = eyed3.load(os.path.join(root, file))
            if mfile.tag.title is None:
                print("No tag for " + file + ".")
            else:
                # print id3 tag into to std out
                #print (mfile.tag.title)
                # load the id3 tags you want into a string
                line = mfile.tag.title
                #s = str(mfile)
                # write out to file
                f.write(line+"\n")
f.close()
