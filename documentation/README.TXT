Haven't decided yet in what format to write the documentation.  Straight HTML?  TXT?

Big picture:

I have my journal files in a directory called ~/journal on my site.

They're basically like this:

~/journal/YYYY/MM/DDfilename.html
~/journal/YYYY/MM/DDfilename.txt

Where YYYY represents years that currently span from 1985 ~ 2016 (quite sparsely on the ends)
MM represents months from 01 to 12
DD represents days from 01 to 30 or so depending on the month

Files ending in .html are dumped straight to the screen.
Files ending in .txt are wrapped with <pre></pre> tags before sent to the screen

There are also some files in this format:
~/journal/YYYY/MM/_DDfilename.html, which are private journal entries.

I am sure there are some other files (for a while I was putting images in the same structure) that
need to be handled somehow.

--------

I'd like to continue using that structure for files so that my existing index files (journal.cgi and
journal.pl) continue to work.

AND, I'd like to have a process that imports all the files (and new ones incrementally) to mySQL so
that they can be searched/mixed/matched/tagged/etc more easily.

Though it should prolly be a separate project, I'd also like a much better way of handling pictures:
  *) realtime crop and resize like fileswarm
  *) ability to tag, write captions for pics
  *) Facebook style tagging would be awesome

The journal system would be able to include pictures in the journal entries easily.  Basically I'd
just want to upload pics, get a URL response which I embed in the journal entry.  (choice of a few
URLs for different sized thumbs, plus link to large size or even better, link to a slideshow of all
the pics in the gallery, with focus on the pic that was clicked.)

--------

The optimal system will allow people to log in to leave comments on entries, which would be emailed
to me, and perhaps (!) examined for spam...  Maybe I can require approval of comments from unknown
people and then let comments publish immediately from known people.

