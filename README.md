# sprawl
Expand urls into one url for each path depth

```
$ echo http://www.domain.com/path/to/something | ./sprawl.py
http://www.domain.com/path/to/something
http://www.domain.com/path/to
http://www.domain.com/path
http://www.domain.com
```

Pipe in a file full of paths to improve your recon coverage. 
