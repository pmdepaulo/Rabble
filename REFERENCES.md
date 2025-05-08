Homework #5:
    Satisfactory Tasks:
        I used this documentation on the Factory class (particularly Faker()):
            https://factoryboy.readthedocs.io/en/stable/reference.html#the-factory-class
        I also referenced this GitHub post about the Faker class (I had trouble with it):
            https://github.com/FactoryBoy/factory_boy/issues/426 
        In order to figure out how to turn the Rabble name into a display name (and have them related),
        I asked the following prompt to ChatGPT, which pointed me in the direction of using a lambda function 
        within LazyAttribute(), and then I chose to use ".title()" to get the effect I wanted:
            "how to use a version of previous attribute string as a new attribute in factory boy"

    Extra Tasks:
        For the Extra Tasks (continuous integration), I did not use any outside sources other than the 
        "CI With GitHub Actions" Lecture Notes"

Homework #4:
    Satisfactory Tasks:
        I did not use any outside sources other than the API lecture notes.
    
    Extra Tasks:
        For the first extra task, I referenced the DRF lecture notes, but to implement support for POST requests,
        I asked the following prompt into ChatGPT: "how to make a stringrelatedfield accept post requests."
        This directed me to SlugRelatedField, which I then looked up and used using this documentation:
        https://www.django-rest-framework.org/api-guide/relations/#slugrelatedfield.

        For the second extra task, I used the following ChatGPT prompts to figure out what frameworks I needed:
            "how to implement a toggle feature inside an api view function for post request"
            "how to use the response (JSON data) from the api to update the frontend button accordingly"
            "indexing into JSON const"
            "how to make html template check JSON variable on render"
        I then used these web resources:
            https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch (using Fetch in JS)
            https://docs.djangoproject.com/en/5.2/howto/csrf/ (CSRF token information)
            https://www.wikihow.com/Change-Button-Color-in-Javascript (button color changing in JavaScript)
            https://docs.djangoproject.com/en/5.2/ref/models/instances/ (making an instance of a model, saving it)
            
Homework #3:
    Satisfactory Tasks:
        For the detail views, I used the CRUD notes alongside the following prompts into ChatGPT:
            "html rendering as plaintext" (for help understanding why my html file wasn't rendering)
            "django view getting unexpected parameter passed in" (for help with a repeated error that I was getting, which 
            was resolved when Chat reminded me to add a parameter into the actual view function)
            "in a views file with django where is the request being passed in from" (to help debug the previous error 
            before I understood what the error meant)
            "does django hold onto past migrations or write over them" (when trying to understand why a previous migration
            error was not resolving even after deleting the buggy line--I then just deleted the migrations manually)
        For help with the PostForm, I asked ChatGPT this prompt: "how to create a django PostForm inside a forms.py file in a django project",
        which gave me a clearer idea of what exactly a form was in Django and how to structure it around my model, Posts. I also used this 
        documentation page: https://docs.djangoproject.com/en/5.2/topics/forms/modelforms/ for help on understanding why my form wasn't
        updating the user alongside it (which then led me to just manually adding the user before saving the form).

    Extra Tasks:
        For implementing the extra tasks, I only used outside sources for the authentication one. I used this developer
        post: https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Authentication, 
        which was recommended by Prof. Sotomayor and gave me the @login_required() method that made authentication fairly
        simple to implement. 

Homework #2:
    For this homework, I wrote all of my models manually. However, I did use ChatGPT 4o to ask about clarification on 
    the type syntax for the model attributes. I used this for models.JSONField() to represent an array, BooleanField to
    represent a boolean, and DateTimeField to represent a timestamp with the auto_now_add and auto_now parameters.

    To migrate the models over to the Django admin interface, I used this article: https://www.freecodecamp.org/news/how-to-set-up-a-django-admin-site/ 

Homework #1:
    Task 1:
        I prompted ChatGPT 4o with the example prompt from the homework writeup: "In a Django template, how could I print one text if the user is logged in, and a different one if no user is logged in?"
        This helped me understand some of the syntax better and use the "is authenticated" Django syntax.

    Task 2:
        I prompted the same AI tool with "get user email address from django user model"
        I realized that it is the same format as user.username with help from an example that the AI tool provided.
  
    Task 3:
        As mentioned in the writeup, it was permitted to paste our base.html code into an AI model to help understand it, so I pasted that code along with the prompt:
        "how can i edit the large block of code above to add a my profile button if a user is logged in"
        This then gave me some code for making a profile button and I used that to make a second Log Out button. 
        Finally, I was curious about how to customize the buttons, so I sent in the prompt "what are the different btn classes" so that I could understand the "btn" types better.
        It gave me a bunch of color customizations and different styles that I chose from to make my Rabble buttons.
        Additionally, I had a Django error that would not let me log out when I was logged in. I was directed to the following 
        site after I asked about this on Slack:
        https://stackoverflow.com/questions/77928535/django-can-login-but-cant-logout-405-method-not-allowed 
        This fixed my issue with the four lines of code that replaced the button instructions with an HTML POST form. 