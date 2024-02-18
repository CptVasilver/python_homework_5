from selene import browser, be, have, command
import pytest
import os


def test_filling_table():
    browser.open('https://demoqa.com/automation-practice-form')

    # filling form
    browser.element('[id="firstName"]').should(be.blank).type('Yashaka')
    browser.element('[id="lastName"]').should(be.blank).type('Selenium')
    browser.element('[id="userEmail"]').should(be.blank).type('Examplum@mulpmaxe.com')
    browser.all('[name=gender]').element_by(have.value_containing('Male')).with_(click_by_js=True).click()
    browser.element('[id="userNumber"]').should(be.blank).type('8005553535')
    browser.element('[id="dateOfBirthInput"]').perform(command.select_all).type('19 Nov 1900').press_enter()
    browser.element('[id="subjectsInput"]').type('Math').press_enter()
    browser.element('[id="hobbies-checkbox-2"]').with_(click_by_js=True).click()
    browser.element('[id="hobbies-checkbox-3"]').with_(click_by_js=True).click()
    browser.element('[id="uploadPicture"]').send_keys(os.path.abspath('pic.png'))
    browser.element('[id="currentAddress"]').should(be.blank).type('Colorado-Springs')
    browser.element('[id="state"]').click().element('[id="react-select-3-option-0"]').click()
    browser.element('[id="city"]').click().element('[id="react-select-4-option-2"]').click()
    browser.element('[id="submit"]').click()

    # check for successfully filled tab
    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))

    # check for correct data
    browser.all('[class="table table-dark table-striped table-bordered table-hover"]>tbody>tr>td').should(
        have.exact_texts(
            'Student Name', 'Yashaka Selenium',
            'Student Email', 'Examplum@mulpmaxe.com',
            'Gender', 'Male',
            'Mobile', '8005553535',
            'Date of Birth', '19 November,1900',
            'Subjects', 'Maths',
            'Hobbies', 'Reading, Music',
            'Picture', 'pic.png',
            'Address', 'Colorado-Springs',
            'State and City', 'NCR Noida'))
    browser.element('[id="closeLargeModal"]').click()
    browser.quit()
