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
