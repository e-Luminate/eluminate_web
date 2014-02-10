from django import template
from events.models import Day

register = template.Library()

@register.filter(name='tidy')
def tidy(theDaysObj):
    """Compresses dates into a minimal string"""

    # make an index of days
    allDays = list(Day.objects.all().order_by('pk'))
    #return type(theDays.all())
    theDays = list(theDaysObj.all())

    s = str(theDays[0])        # the first (and maybe the only) day in the list
    if len(theDays) == 2:      # only two days, so comma list them
        s += ", " + str(theDays[1])
    if len(theDays)>2:         # more than two days, so look for ranges we can replace with a hyphen
        for t in range(1,len(theDays)-1):
            i = allDays.index(theDays[t]) 
            if ((allDays.index(theDays[t-1]) == i-1) and (allDays.index(theDays[t+1]) == i+1)):
                # it is in the middle of a range...
                if s[-2:] != "- ": # if it's the first day of a range, put in the hypehn
                    s += " - "
            else: # it's either the start/end of a range, or a one-off
                if s[-2:] != "- ": # it's the start or a one-off -- needs a comma in both cases
                    s += ", "
                s += str(theDays[t]) # and in all three cases, we need the date itself.
        if s[-2:] != "- ":
            s = s + ", "
        s +=  str(theDays[-1])
    return s

@register.filter(name='makeDateClasses')
def makeDateClasses(theDaysObj):
    """creates a string of css classes from the days object, with leading space"""
    classList = " dayall"

    # make an index of days
    allDays = list(Day.objects.all().order_by('pk'))

    for day in list(theDaysObj.all()):
        i=allDays.index(day)
        classList += " day"+str(i)
    return classList

@register.assignment_tag
def dateList():
    # make an index of days
    allDays = list(Day.objects.all().order_by('pk'))
    r=[]
    for day in allDays:
        r.append((str(day).split(" "))[1][:-2])
    return r

@register.simple_tag
def dateTickBoxes():
    # make an index of days
    allDays = list(Day.objects.all().order_by('pk'))

    r= """
    <script>
$(document).ready(function(){ 
  $("input[name=dateTickBoxes]").bind('change', function(){
    newDate = jQuery( 'input[name=dateTickBoxes]:checked' ).val();
    if (newDate == "all") {
      $(".dayall").show();
    }
    else
    {
      $(".dayall").hide();
      $("."+newDate).show();
    }
  }); 
});
    </script>
    <div class="row-fluid">
    <form action="">
    <label style='white-space: nowrap; display: inline''><input type='radio' name='dateTickBoxes' value ='all' checked> All days</label> 
    """
    for day in allDays:
        r+=" <label style='white-space: nowrap; display: inline'><input type='radio' name='dateTickBoxes' value='day"+str(allDays.index(day))+"'> "+(str(day).split(" "))[1]+"</label>"
    r+="</div>"
    return r

@register.filter(name='booleanDates')
def booleanDates(theDaysObj):
    """Compresses dates into a list of True/False"""

    # make an index of days
    allDays = list(Day.objects.all().order_by('pk'))
    #return type(theDays.all())
    theDays = list(theDaysObj.all())

    l = []

    for today in allDays:
        try:
            i= theDays.index(today)
            l.append(True)
        except:
            l.append(False)
    return l
