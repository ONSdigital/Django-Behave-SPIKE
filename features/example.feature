Feature: Example scenarios

    Scenario: External user can see the homepage
        When An external user navigates to the ONS website
        Then they can see the title ONS Static Site Template
        And they can see the text Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ornare nisl ac dolor dapibus, non mattis sapien egestas.


    Scenario: External user can see the cookies page
        When An external user navigates to the ONS website
        Then they click on the Cookies link
        Then they can see the title Cookies on the cookies page
