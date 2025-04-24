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
        which gave me several different methods that I used to implement the login authorization. I also asked ChatGPT
        the following prompt: "how to take a user back to the login screen in a views file django", which then informed me 
        that my problem could be solved using a previous technique that we had used (reverse()). 

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