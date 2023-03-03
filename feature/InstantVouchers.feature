Feature: Instant Vouchers Page

 Scenario: To validate user navigation to Instant vouchers page
   Given launch chrome browser and payback application is launched
   When user hovers on earn points and selects instant vouchers link
   Then user is navigated to Instant Vouchers page


 Scenario:To validate user can enter text in the search bar
    Given launch chrome browser and payback application is launched
   When user hovers on earn points and selects instant vouchers link
   Then user is navigated to Instant Vouchers page
   And user enters text in the search bar



 Scenario: To validate user can get relevant result by clicking on search logo
    Given launch chrome browser and payback application is launched
   When user hovers on earn points and selects instant vouchers link
   Then user is navigated to Instant Vouchers page
   And user enters text in the search bar
   Then user clicks on search icon
   Then the page is reloaded

 Scenario: To validate user remains on the same page when enters an invalid text
   Given launch chrome browser and payback application is launched
   When user hovers on earn points and selects instant vouchers link
   Then user is navigated to Instant Vouchers page
   And user enters invalid text in the search bar
   Then user clicks on search icon
   And user remains on the same page

 Scenario: to validate the user can select the relevant result which are displayed below the search bar while entering the text
   Given launch chrome browser and payback application is launched
   When user hovers on earn points and selects instant vouchers link
   Then user is navigated to Instant Vouchers page
   And user enters text in the search bar
   Then user clicks on search icon
   Then the page is reloaded
   Then user selects dropdown text which is displayed


 Scenario: To validate that the chat box has appeared when the user clicks on chat assistant logo
   Given launch chrome browser and payback application is launched
   When user hovers on earn points and selects instant vouchers link
   Then user is navigated to Instant Vouchers page
   Then user clicks on chat assistant logo

   Scenario: To validate the user is able to click on any of the displayed options
     Given launch chrome browser and payback application is launched
   When user hovers on earn points and selects instant vouchers link
   Then user is navigated to Instant Vouchers page
   Then user clicks on chat assistant logo
    Then user clicks on i have a voucher button











