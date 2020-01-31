# Prevent hidden page elements from reappearing on page reload

## Overview
In some cases it is desirable to hide certain parts of the page after a given time period. Let's say you want to let participants in your experiment chat for 60 seconds before making their decision on the same screen. In this case, normal page timeouts are not helpful. You might resort to  hidding the chat box or its inputs by setting their ```display``` property to ``hidden`` after a Javascript timeout. Problems arise if participants reload the page which causes the elements to reappear and the Javascript countdown to reset.

This code snippet shows how user interface elements can be prevented from reappearing and the timer from resetting on page reload.

## Explanation
When a page is loaded in oTree, the ``vars_for_template`` method is called. In the snippet, the timestamp of the first time a participant loads the page and triggers the ``vars_for_template`` method is stored in a dedicated field on the player model. On subsequent (re-)loads of the same page, the timestamp is not updated but read from the database. See ``models.py`` and ``pages.py`` in the ``hide_elemets`` app.

The timestamp is passed on to the template, where a small script checks whether the current timestamp is more than X seconds larger than the timestamp created when the page was first loaded (X is the time the user interface element should be visible for). If the current timestamp is larger, the interface element is not shown. If it is smaller, we repeat the check every second until the time has elapsed and the element is hidden. See the scripts block in ``MyPage.html`` in ``hide_elements/templates/hide_elements``.

While this is clearly not the intended use of ``vars_for_template``, it is a simple solution to the problem and only uses the tools readily available in oTree.