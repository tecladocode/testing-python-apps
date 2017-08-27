Feature: Test navigation between pages
  Make sure homepage can go to blog, and
  blog can go to homepage

  Scenario: Homepage can go to Blog
    Given I am on the homepage
    When I click on the link with id "blog-link"
    Then I am on the blog page

  Scenario: Blog page can go to homepage
    Given I am on the blog page
    When I click on the link with id "home-link"
    Then I am on the homepage

  Scenario: Blog page has an appropriate title
    Given I am on the blog page
    Then There is a h1 tag with the content "This is the blog page"

  Scenario: Homepage has an appropriate title
    Given I am on the homepage
    Then There is a h1 tag with the content "This is the homepage"