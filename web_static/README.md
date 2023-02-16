# 0x01. AirBnB clone - Web static

<div class="panel-body">

<p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230207%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20230207T190050Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=3c97d690d5799e5d196c4a32f2601ddfa3515f2c47ef518f16067afff3233af1" alt="" loading="lazy" style=""></p>

<h2>Background Context</h2>


<p>Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!</p>

<p>Before developing a big and complex web application, we will build the front end step-by-step. </p>

<p>The first step is to “design” / “sketch” / “prototype” each element:</p>

<ul>
<li>Create simple HTML static pages</li>
<li>Style guide</li>
<li>Fake contents</li>
<li>No Javascript</li>
<li>No data loaded from anything</li>
</ul>

<p>During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.</p>

<p>Before starting, please fork or clone the repository <code>AirBnB_clone</code> from your partner if you were not the owner of the previous project.</p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/T9KyiA6_Tm3Ny6oTn08S-A" title="Learn to Code HTML &amp; CSS" target="_blank">Learn to Code HTML &amp; CSS</a> (<em>until “Creating Lists” included</em>)</li>
<li><a href="/rltoken/7NdYbImFNofpB_FXXn3otg" title="Inline Styles in HTML" target="_blank">Inline Styles in HTML</a> </li>
<li><a href="/rltoken/z_OTPFCjmhXJJi7KJqBCbQ" title="Specifics on CSS Specificity" target="_blank">Specifics on CSS Specificity</a> </li>
<li><a href="/rltoken/7iqk-el4ZVnKeyLoON8Rqg" title="CSS SpeciFishity" target="_blank">CSS SpeciFishity</a> </li>
<li><a href="/rltoken/okP4V3RxFXHkEcQo19AnuQ" title="Introduction to HTML" target="_blank">Introduction to HTML</a> </li>
<li><a href="/rltoken/Ir8Ka59FO6Z_vJQ-gkSG_w" title="CSS" target="_blank">CSS</a> </li>
<li><a href="/rltoken/BpSXtcWOGH0UT4XLCoQyJg" title="MDN" target="_blank">MDN</a> </li>
<li><a href="/rltoken/Tlje4XYwyZbUfHkQWGi1WQ" title="center boxes" target="_blank">center boxes</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/Zb9sTIct2xdhDCDLGF-RyQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is HTML</li>
<li>How to create an HTML page</li>
<li>What is a markup language</li>
<li>What is the DOM</li>
<li>What is an element / tag</li>
<li>What is an attribute</li>
<li>How does the browser load a webpage</li>
<li>What is CSS</li>
<li>How to add style to an element</li>
<li>What is a class</li>
<li>What is a selector</li>
<li>How to compute CSS Specificity Value</li>
<li>What are Box properties in CSS</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should be W3C compliant and validate with <a href="/rltoken/NzQ96QXtBTCMRDicPORzbA" title="W3C-Validator" target="_blank">W3C-Validator</a></li>
<li>All your CSS files should be in <code>styles</code> folder</li>
<li>All your images should be in <code>images</code> folder</li>
<li>You are not allowed to use <code>!important</code> and <code>id</code> (<code>#...</code> in the CSS file)</li>
<li>You are not allowed to use tags <code>img</code>, <code>embed</code> and <code>iframe</code></li>
<li>You are not allowed to use Javascript</li>
<li>Current screenshots have been done on <code>Chrome 56</code> or more. </li>
<li>No cross browsers </li>
<li>You have to follow all requirements but some <code>margin</code>/<code>padding</code> are missing - you should try to fit as much as you can to screenshots</li>
</ul>

<h2>More Info</h2>

<p><img src="https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step1.png" alt="" loading="lazy" style=""></p>

<h2>Tasks</h2>


<div class="panel-body">

<h4>0. Inline styling</h4>
<p>Write an HTML page that displays a header and a footer.</p>

<p>Layout:</p>

<ul>
<li>Body:

<ul>
<li>no margin</li>
<li>no padding</li>
</ul></li>
<li>Header:

<ul>
<li>color #FF0000 (red)</li>
<li>height: 70px</li>
<li>width: 100%</li>
</ul></li>
<li>Footer:

<ul>
<li>color #00FF00 (green)</li>
<li>height: 60px</li>
<li>width: 100%</li>
<li>text <code>Best School</code> center vertically and horizontally</li>
<li>always at the bottom at the page</li>
</ul></li>
</ul>

<p>Requirements:</p>

<ul>
<li>You must use the <code>header</code> and <code>footer</code> tags</li>
<li>You are not allowed to import any files</li>
<li>You are not allowed to use the <code>style</code> tag in the <code>head</code> tag</li>
<li>Use inline styling for all your tags</li>
</ul>

<p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/98f4ac1b0644512ce7ae91a9e8e61e8fe174911d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230216%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20230216T123105Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=a82d3fd6d567041c785c765738eadc4ed73e212aa85993e7ebe22e7d025ac618" alt="" loading="lazy" style="width: 100%"></p>

  </div>


<h4>1. Head styling</h4>
<div class="panel-body">
 <p>Write an HTML page that displays a header and a footer by using the <code>style</code> tag in the</p>

<p>Requirements:</p>

<ul>
<li>You must use the <code>header</code> and <code>footer</code> tags</li>
<li>You are not allowed to import any files</li>
<li>No inline styling</li>
<li>You must use the <code>style</code> tag in the <code>head</code> tag</li>
</ul>

<p>The layout must be exactly the same as <code>0-index.html</code></p>
</div>

<div class="panel-body">

### 2. CSS files
<p>Write an HTML page that displays a header and a footer by using CSS files (same as <code>1-index.html</code>)</p>

<p>Requirements:</p>

<ul>
<li>You must use the <code>header</code> and <code>footer</code> tags</li>
<li>No inline styling</li>
<li>You must have 3 CSS files:

<ul>
<li><code>styles/2-common.css</code>: for global style (i.e. the <code>body</code> style)</li>
<li><code>styles/2-header.css</code>: for header style</li>
<li><code>styles/2-footer.css</code>: for footer style</li>
</ul></li>
</ul>

<p>The layout must be exactly the same as <code>1-index.html</code></p>

</div>

### 3. Zoning done!
Write an HTML page that displays a header and footer by using CSS files (same as  `2-index.html`)

Layout:

-   Common:
    -   no margin
    -   no padding
    -   font color: #484848
    -   font size: 14px
    -   font family:  `Circular,"Helvetica Neue",Helvetica,Arial,sans-serif;`
    -   [icon](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon.png "icon")  in the browser tab
-   Header:
    -   color: white
    -   height: 70px
    -   width: 100%
    -   border bottom 1px #CCCCCC
    -   [logo](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/logo.png "logo")  align on left and center vertically (20px space at the left)
-   Footer:
    -   color white
    -   height: 60px
    -   width: 100%
    -   border top 1px #CCCCCC
    -   text  `Best School`  center vertically and horizontally
    -   always at the bottom at the page

Requirements:

-   No inline style
-   You are not allowed to use the  `img`  tag
-   You are not allowed to use the  `style`  tag in the  `head`  tag
-   All images must be stored in the  `images`  folder
-   You must have 3 CSS files:
    -   `styles/3-common.css`: for the global style (i.e  `body`  style)
    -   `styles/3-header.css`: for the header style
    -   `styles/3-footer.css`: for the footer style

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/2be1eda05a0d9097c210f2d3482a59aa858c5711.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230216%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230216T123105Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5284d78d3f8584c097f38d4da5604a51e3e81a19188a2f88d4e0900bba332679)

### 4. Search!
Write an HTML page that displays a header, footer and a filters box with a search button.

Layout: (based on  `3-index.html`)

-   Container:
    -   between  `header`  and  `footer`  tags, add a  `div`:
        -   classname:  `container`
        -   max width 1000px
        -   margin top and bottom 30px - it should be 30px under the bottom of the  `header`  (screenshot)
        -   center horizontally
-   Filter section:
    -   tag  `section`
    -   classname  `filters`
    -   inside the  `.container`
    -   color white
    -   height: 70px
    -   width: 100% of the container
    -   border 1px #DDDDDD with radius 4px
-   Button search:
    -   tag  `button`
    -   text  `Search`
    -   font size: 18px
    -   inside the section filters
    -   background color #FF5A5F
    -   text color #FFFFFF
    -   height: 48px
    -   width: 20% of the section filters
    -   no borders
    -   border radius: 4px
    -   center vertically and at 30px of the right border
    -   change opacity to 90% when the mouse is on the button

Requirements:

-   You must use:  `header`,  `footer`,  `section`,  `button`  tags
-   No inline style
-   You are not allowed to use the  `img`  tag
-   You are not allowed to use the  `style`  tag in the  `head`  tag
-   All images must be stored in the  `images`  folder
-   You must have 4 CSS files:
    -   `styles/4-common.css`: for the global style (`body`  and  `.container`  styles)
    -   `styles/3-header.css`: for the header style
    -   `styles/3-footer.css`: for the footer style
    -   `styles/4-filters.css`: for the filters style
-   `4-index.html`  **won’t be W3C valid**, don’t worry, it’s temporary

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/f959154b0cdf1cdf71ddef04e3787ef28462793e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230216%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230216T123105Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7305ecaa6b0e0d853bf4c642143db7b8c523fb52fae4a9105b4e0106346b2d7d)


### 5. More filters
Write an HTML page that displays a header, footer and a filters box.

Layout: (based on  `4-index.html`)

-   Locations and Amenities filters:
    -   tag:  `div`
    -   classname:  `locations`  for location tag and  `amenities`  for the other
    -   inside the section filters (same level as the  `button`  Search)
    -   height: 100% of the section filters
    -   width: 25% of the section filters
    -   border right #DDDDDD 1px only for the first left filter
    -   contains a title:
        -   tag:  `h3`
        -   font weight: 600  
            
        -   text  `States`  or  `Amenities`
    -   contains a subtitle:
        -   tag:  `h4`
        -   font weight: 400  
            
        -   font size: 14px
        -   text with fake contents

Requirements:

-   You must use:  `header`,  `footer`,  `section`,  `button`,  `h3`,  `h4`  tags
-   No inline style
-   You are not allowed to use the  `img`  tag
-   You are not allowed to use the  `style`  tag in the  `head`  tag
-   All images must be stored in the  `images`  folder
-   You must have 4 CSS files:
    -   `styles/4-common.css`: for the global style (`body`  and  `.container`  styles)
    -   `styles/3-header.css`: for the header style
    -   `styles/3-footer.css`: for the footer style
    -   `styles/5-filters.css`: for the filters style

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/85bfa50b96c2985723daa75b5e22f75ef16e2b2e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230216%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230216T123105Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=936fa8481a2f30781f56e7cc8812b4dada999337e6df132e55dc50a1f954ff97)


### 6. It's (h)over
Write an HTML page that displays a header, footer and a filters box with dropdown.

Layout: (based on  `5-index.html`)

-   Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter  `div`:
    -   tag  `ul`
    -   classname  `popover`
    -   text should be fake now
    -   inside each  `div`
    -   not displayed by default
    -   color #FAFAFA
    -   width same as the  `div`  filter
    -   border #DDDDDD 1px with border radius 4px
    -   no list display
    -   Location filter has 2 levels of  `ul`/`li`:
        -   state -> cities
        -   state name must be display in a  `h2`  tag (font size 16px)

Requirements:

-   You must use:  `header`,  `footer`,  `section`,  `button`,  `h3`,  `h4`,  `ul`,  `li`  tags
-   No inline style
-   You are not allowed to use the  `img`  tag
-   You are not allowed to use the  `style`  tag in the  `head`  tag
-   All images must be stored in the  `images`  folder
-   You must have 4 CSS files:
    -   `styles/4-common.css`: for the global style (`body`  and  `.container`  styles)
    -   `styles/3-header.css`: for the header style
    -   `styles/3-footer.css`: for the footer style
    -   `styles/6-filters.css`: for the filters style

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/6262f13624dca23ca19db505c44f88faddb82ebb.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230216%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230216T123105Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6aa0e3370fc81def05739009e722d02a708a106da4367093a0a5cb27704ee138)  ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/6e6bdfa13fa88a5f439d9e2b1dade826dd95529b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230216%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230216T123105Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=55171f20904905a32f587a610cf755a6974e4214a0b762f30f471aa5d7887620)


### 7. Display results
Write an HTML page that displays a header, footer, a filters box with dropdown and results.

Layout: (based on  `6-index.html`)

-   Add Places section:
    -   tag:  `section`
    -   classname:  `places`
    -   same level as the filters section, inside  `.container`
    -   contains a title:
        -   tag:  `h1`
        -   text:  `Places`
        -   align in the top left
        -   font size: 30px
    -   contains multiple “Places” as listing (horizontal or vertical) describe by:
        -   tag:  `article`
        -   width: 390px
        -   padding and margin 20px
        -   border #FF5A5F 1px with radius 4px
        -   contains the place name:
            -   tag:  `h2`
            -   font size: 30px
            -   center horizontally

Requirements:

-   You must use:  `header`,  `footer`,  `section`,  `article`,  `button`,  `h1`,  `h2`,  `h3`,  `h4`,  `ul`,  `li`  tags
-   No inline style
-   You are not allowed to use the  `img`  tag
-   You are not allowed to use the  `style`  tag in the  `head`  tag
-   All images must be stored in the  `images`  folder
-   You must have 5 CSS files:
    -   `styles/4-common.css`: for the global style (i.e.  `body`  and  `.container`  styles)
    -   `styles/3-header.css`: for the header style
    -   `styles/3-footer.css`: for footer style
    -   `styles/6-filters.css`: for the filters style
    -   `styles/7-places.css`: for the places style

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/bca4d17fbe21a58b66a9d5d6b85df4801d147dd0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230216%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230216T123105Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a563df1be367c1da31538e867588d8a1ec8fff9bcdb530c26a6032c1afce5a63)

### 8. More details
Write an HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search.

Layout: (based on  `7-index.html`)

Add more information to a Place  `article`:

-   Price by night:
    -   tag:  `div`
    -   classname:  `price_by_night`
    -   same level as the place name
    -   font color: #FF5A5F
    -   border: #FF5A5F 4px rounded
    -   min width: 60px
    -   height: 60px
    -   font size: 30px
    -   align: the top right (with space)
-   Information section:
    -   tag:  `div`
    -   classname:  `information`
    -   height: 80px
    -   border: top and bottom #DDDDDD 1px
    -   contains (align vertically):
        -   Number of guests:
            -   tag:  `div`
            -   classname:  `max_guest`
            -   width: 100px
            -   fake text
            -   [icon](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_group.png "icon")
        -   Number of bedrooms:
            -   tag:  `div`
            -   classname:  `number_rooms`
            -   width: 100px
            -   fake text
            -   [icon](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_bed.png "icon")
        -   Number of bathrooms:
            -   tag:  `div`
            -   classname:  `number_bathrooms`
            -   width: 100px
            -   fake text
            -   [icon](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_bath.png "icon")
-   User section:
    -   tag:  `div`
    -   classname:  `user`
    -   text  `Owner: <fake text>`
    -   `Owner`  text should be in bold
-   Description section:
    -   tag:  `div`
    -   classname:  `description`

Requirements:

-   You must use:  `header`,  `footer`,  `section`,  `article`,  `button`,  `h1`,  `h2`,  `h3`,  `h4`,  `ul`,  `li`  tags
-   No inline style
-   You are not allowed to use the  `img`  tag
-   You are not allowed to use the  `style`  tag in the  `head`  tag
-   All images must be stored in the  `images`  folder
-   You must have 5 CSS files:
    -   `styles/4-common.css`: for the global style (i.e.  `body`  and  `.container`  styles)
    -   `styles/3-header.css`: for the header style
    -   `styles/3-footer.css`: for the footer style
    -   `styles/6-filters.css`: for the filters style
    -   `styles/8-places.css`: for the places style

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/f4b2d4ef94bd3a2e7e1ddefa81236595686d270e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230216%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230216T123105Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=042228cbf33e73fc2a2bfbace7431cdab82b310f55ac6875f72f5b65889327cb)


### 9. Full details
Write an HTML page that displays a header, footer, a filters box with dropdown and results.

Layout: (based on  `8-index.html`)

Add more information to a Place  `article`:

-   List of Amenities:
    -   tag  `div`
    -   classname  `amenities`
    -   margin top 40px
    -   contains:
        -   title:
            -   tag  `h2`
            -   text  `Amenities`
            -   font size 16px
            -   border bottom #DDDDDD 1px
        -   list of amenities:
            -   tag  `ul`  /  `li`
            -   no list style
            -   icons on the left:  [Pet friendly](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_pets.png "Pet friendly"),  [TV](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_tv.png "TV"),  [Wifi](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_wifi.png "Wifi"), etc… feel free to add more
-   List of Reviews:
    -   tag  `div`
    -   classname  `reviews`
    -   margin top 40px
    -   contains:
        -   title:
            -   tag  `h2`
            -   text  `Reviews`
            -   font size 16px
            -   border bottom #DDDDDD 1px
        -   list of review:
            -   tag  `ul`  /  `li`
            -   no list style
            -   a review is described by:
                -   `h3`  tag for the user/date description (font size 14px). Ex: “From Bob Dylan the 27th January 2017”
                -   `p`  tag for the text (font size 12px)

Requirements:

-   You must use:  `header`,  `footer`,  `section`,  `article`,  `button`,  `h1`,  `h2`,  `h3`,  `h4`,  `ul`,  `li`  tags
-   No inline style
-   You are not allowed to use the  `img`  tag
-   You are not allowed to use the  `style`  tag in the  `head`  tag
-   All images must be stored in the  `images`  folder
-   You must have 5 CSS files:
    -   `styles/4-common.css`: for the global style (`body`  and  `.container`  styles)
    -   `styles/3-header.css`: for the header style
    -   `styles/3-footer.css`: for the footer style
    -   `styles/6-filters.css`: for the filters style
    -   `styles/100-places.css`: for the places style

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/f54486a431a05ea3477e337e0e953686d3c6ffd0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230216%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230216T123105Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2e6e820ffba3db8dcc4ca0e88e11aade23e96c3d2d6edb7e5b19e254e3add9bc)


### 10. Flex
Improve the Places section by using  [Flexible boxes](https://intranet.alxswe.com/rltoken/Xc-nBlQHexwNaCuKYpZ2-A "Flexible boxes")  for all Place articles

[Flexbox Froggy](https://intranet.alxswe.com/rltoken/PZz46Gkdj5Mo9-AWERPhQA "Flexbox Froggy")

### 11. Responsive design
Improve the page by adding  [responsive design](https://intranet.alxswe.com/rltoken/9mRhZcLRxmsuCyF8q7S8Ww "responsive design")  to display correctly in mobile or small screens.

Examples:

-   no horizontal scrolling
-   redesign search bar depending of the width
-   etc.

### 12. Accessibility
Improve the page by adding  [Accessibility support](https://intranet.alxswe.com/rltoken/JO-zonPvzBUfqpYRZDAtug "Accessibility support")

Examples:

-   Colors contrast
-   Header tags
-   etc.

</div>
