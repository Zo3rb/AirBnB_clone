#  0x00. AirBnB clone - The console
<div class="panel-body">
    <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230207%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20230207T190050Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=3c97d690d5799e5d196c4a32f2601ddfa3515f2c47ef518f16067afff3233af1" alt="" loading="lazy" style=""></p>

<h2>Background Context</h2>

<h3>Welcome to the AirBnB clone project!</h3>

<p>Before starting, please read the <strong>AirBnB</strong> concept page.</p>

<p><br></p>

[![SE - HBNB - Project Overview](https://youtu.be/1mAC9x3aixE)](https://youtu.be/1mAC9x3aixE)

<p><br></p>

<h4>First step: Write a command interpreter to manage your AirBnB objects.</h4>

<p>This is the first step towards building your first full web application: the <strong>AirBnB clone</strong>.
This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration… </p>

<p>Each task is linked and will help you to:</p>

<ul>
<li>put in place a parent class (called <code>BaseModel</code>) to take care of the initialization, serialization and deserialization of your future instances</li>
<li>create a simple flow of serialization/deserialization: Instance &lt;-&gt; Dictionary &lt;-&gt; JSON string &lt;-&gt; file</li>
<li>create all classes used for AirBnB (<code>User</code>, <code>State</code>, <code>City</code>, <code>Place</code>…) that inherit from <code>BaseModel</code></li>
<li>create the first abstracted storage engine of the project: File storage. </li>
<li>create all unittests to validate all our classes and storage engine</li>
</ul>

<h3>What’s a command interpreter?</h3>

<p>Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:</p>

<ul>
<li>Create a new object (ex: a new User or a new Place)</li>
<li>Retrieve an object from a file, a database etc…</li>
<li>Do operations on objects (count, compute stats, etc…)</li>
<li>Update attributes of an object</li>
<li>Destroy an object</li>
</ul>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/8ecCwE6veBmm3Nppw4hz5A" title="cmd module" target="_blank">cmd module</a> </li>
<li><a href="/rltoken/uEy4RftSdKypoig9NFTvCg" title="cmd module in depth" target="_blank">cmd module in depth</a></li>
<li><strong>packages</strong> concept page</li>
<li><a href="/rltoken/KfL9TqwdI69W6ttG6gTPPQ" title="uuid module" target="_blank">uuid module</a> </li>
<li><a href="/rltoken/1d8I3jSKgnYAtA1IZfEDpA" title="datetime" target="_blank">datetime</a> </li>
<li><a href="/rltoken/IlFiMB8UmqBG2CxA0AD3jA" title="unittest module" target="_blank">unittest module</a> </li>
<li><a href="/rltoken/C_a0EKbtvKdMcwIAuSIZng" title="args/kwargs" target="_blank">args/kwargs</a> </li>
<li><a href="/rltoken/tgNVrKKzlWgS4dfl3mQklw" title="Python test cheatsheet" target="_blank">Python test cheatsheet</a> </li>
<li><a href="/rltoken/EvcaH9uTLlauxuw03WnkOQ" title="cmd module wiki page" target="_blank">cmd module wiki page</a></li>
<li><a href="/rltoken/begh14KQA-3ov29KvD_HvA" title="python unittest" target="_blank">python unittest</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="#" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>How to create a Python package</li>
<li>How to create a command interpreter in Python using the <code>cmd</code> module</li>
<li>What is Unit testing and how to implement it in a large project</li>
<li>How to serialize and deserialize a Class</li>
<li>How to write and read a JSON file</li>
<li>How to manage <code>datetime</code></li>
<li>What is an <code>UUID</code></li>
<li>What is <code>*args</code> and how to use it</li>
<li>What is <code>**kwargs</code> and how to use it</li>
<li>How to handle named arguments in a function</li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version <code>2.8.*</code>)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>

<h3>Python Unit Tests</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files should end with a new line</li>
<li>All your test files should be inside a folder <code>tests</code></li>
<li>You have to use the <a href="/rltoken/op1-rQGlw0wwwqNBsn1yaw" title="unittest module" target="_blank">unittest module</a> </li>
<li>All your test files should be python files (extension: <code>.py</code>)</li>
<li>All your test files and folders should start by <code>test_</code></li>
<li>Your file organization in the tests folder should be the same as your project</li>
<li>e.g., For <code>models/base_model.py</code>, unit tests must be in: <code>tests/test_models/test_base_model.py</code></li>
<li>e.g., For <code>models/user.py</code>, unit tests must be in: <code>tests/test_models/test_user.py</code></li>
<li>All your tests should be executed by using this command: <code>python3 -m unittest discover tests</code></li>
<li>You can also test file by file by using this command: <code>python3 -m unittest tests/test_models/test_base_model.py</code></li>
<li>All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>We strongly encourage you to work together on test cases, so that you don’t miss any edge case</li>
</ul>

<h2>More Info</h2>

<h3>Execution</h3>

<p>Your shell should work like this in interactive mode:</p>

<pre><code>$ ./console.py
(hbnb) help

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
</code></pre>

<p>But also in non-interactive mode: (like the Shell project in C)</p>

<pre><code>$ echo "help" | ./console.py
(hbnb)

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit
(hbnb) 
$
</code></pre>

<p>All tests should also pass in non-interactive mode: <code>$ echo "python3 -m unittest discover tests" | bash</code></p>

<p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230207%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20230207T190050Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=25c520d30cb6aea87551b93692a9f4d0f56e92160d559681e5754f9c4b0520c6" alt="" loading="lazy" style=""></p>

<p><br></p>

[![SE - HBNB - The Console](https://www.youtube.com/embed/1mAC9x3aixE)](https://www.youtube.com/embed/1mAC9x3aixE)

  </div>

<h4>AUTHORS:</h4>
<h5><a href="https://github.com/Zo3rb">Ali Fakhri</a></h5>
<h5><a href="https://github.com/ismailadebiyi">Adebiyi Adebiyi</a></h5>

