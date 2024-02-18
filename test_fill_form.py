from selene import browser, be, have, command
import os


def test_filling_table():
    browser.open('/')
    # filling form
    browser.element('#firstName').should(be.blank).type('Yashaka')
    browser.element('#lastName').should(be.blank).type('Selenium')
    browser.element('#userEmail').should(be.blank).type('Examplum@mulpmaxe.com')
    browser.all('[name=gender]').element_by(have.value_containing('Male')).with_(click_by_js=True).click()
    browser.element('#userNumber').should(be.blank).type('8005553535')
    browser.element('#dateOfBirthInput').perform(command.select_all).type('19 Nov 1900').press_enter()
    browser.element('#subjectsInput').type('Math').press_enter()
    browser.element('#hobbies-checkbox-2').with_(click_by_js=True).click()
    browser.element('#hobbies-checkbox-3').with_(click_by_js=True).click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('pic.png'))
    browser.element('#currentAddress').should(be.blank).type('Colorado-Springs')
    browser.element('#state').click().element('#react-select-3-option-0').click()
    browser.element('#city').click().element('#react-select-4-option-2').click()
    browser.element('#submit').click()

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
    browser.element('#closeLargeModal').click()
