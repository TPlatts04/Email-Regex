from email_regex import email_test_reg

def test_email():
    assert email_test_reg("hellothere@gmail.com") ==  True
    assert email_test_reg("hellothere@hotmail.co.uk") == True
    assert email_test_reg("hellothere@outlook.net") == True 
    assert email_test_reg("hellothere@yahoo.org") == True
    assert email_test_reg("thisisaverylongemailandthiswillbepassingthelengthboundariessetbytheregex@gmail.com") == None
    assert email_test_reg(".testemail@gmail.com") == None
    assert email_test_reg("testeremail.@gmail.com") == None
    assert email_test_reg("mainemail@@gmail.com") == None
    assert email_test_reg("hellothere@edu.gmail.com") == True
    assert email_test_reg("test..email@gmail.com") == None
    assert email_test_reg("HeLLoTheRe@gmail.com") ==  True
    assert email_test_reg("hellothere@educ41on.learn-now.gmail.com") ==  True