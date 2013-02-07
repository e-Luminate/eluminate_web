/* Basic site JavaScript for SpenceJones.com development
** (C) 2005-2013 SpenceJones.com
*/


// ************* Scrollfunctions ************

var itemOffsets = new Array();	// stores distance to the left edge of each element
var itemCount;					// number of items in the thumbnail list
var currentLeftItem = 0;		// keep track of how far across the thumbnails have scrolled
								// not altered by resize
var maxLeftItem;				// how far we scroll before we can see the right hand item

/* Model
#menu                  Visible window...                   |----------------------|
#participant_selector  set of elements...  |-0-|--1--|--2--|--3---|--4--|--5---|--6--|--7--|---8---|
                       negative margin...  |<------------->|
            after init, total width of all the elements is itemOffsets[itemCount]
*/

function init ()
// count the elements in the scroll, and work out negative margin to make it the first
// needs to be added to <body onLoad="init();" onResize="init();">
{
  thumbnails = document.getElementById("participant_selector");
    elements = thumbnails.getElementsByTagName("a"); // array of img elements
  
  // measure the cumulative offset to each element
  itemOffsets[0]=0;
  for (itemCount=0; itemCount<elements.length; itemCount++) // nb uses global itemCount (deliberately, to leave it with final value)
  {
      itemOffsets[itemCount+1] = itemOffsets[itemCount] + elements[itemCount].offsetWidth;
  }

  document.getElementById("participant_selector").style.width=itemOffsets[itemCount]+"px" // set the width of the string of images
  
  // now calculate the furthest you'd want to scroll...
  maxLeftItem = 0;
    while (document.getElementById("menu").offsetWidth + itemOffsets[maxLeftItem] < itemOffsets[itemCount]) maxLeftItem++;
  
  // because this function is called on resize, we may have to fix things if we've scrolled too far for new wider window...
  if (currentLeftItem>=maxLeftItem) {
    document.getElementById("participant_selector").style.marginLeft = -itemOffsets[maxLeftItem] +"px";
  }
}

function doScrollLeft() {
  if (currentLeftItem<maxLeftItem) {
    document.getElementById("participant_selector").style.marginLeft = -itemOffsets[++currentLeftItem] +"px";
  }
}

function doScrollRight() {
  if (currentLeftItem>0) {
    document.getElementById("participant_selector").style.marginLeft = -itemOffsets[--currentLeftItem] +"px";
  }
}

// ************* Menu functions *************

function showNav (on)
{
  menuOpen=on;
  if (!tTime) tTime = setTimeout("doTick()",0); // schedule timer event if necessary
}

function doTick ()
{
  tTime=0; // job done!
  if ( ( menuOpen && (mPercent < 99) ) || (!menuOpen && (mPercent > 0)) ) {
    // service timer to expand/contract menu
    ob=document.getElementById('nav-popup').style; // find the menu
    mPercent+= menuOpen?3:-3;               // increment or decrement mPercent
    h=mPercent*1.55;
    w=mPercent*0.50;
    ob.clip="rect("+(155-h)+","+(50+w)+","+(155+h)+","+(50-w)+")";
    ob.visibility=((mPercent>0)?'visible':'hidden');
    tTime=setTimeout('doTick()', 0); // schedule more activity
  }
}

var menuOpen = false; // whether desired state of menu is open or not.
var mPercent = 0;     // how much of menu is currently showing
var tTime    = 0;     // set to the timer magic number when timer is running

// ************* END Menu functions ************


// ************* Preload images *************

function preload() {
for (var x=0; x<preload.arguments.length; x++){
  myimages[x] = new Image();
  myimages[x].src = preload.arguments[x];
  }
}
var myimages = new Array();