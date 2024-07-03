import unittest

step_list = []
step_no = 1


def test_result(status, desc, duration, assertion_message):
    global step_list
    global step_no
    step_list.append((step_no, status, desc, duration, assertion_message))
    step_no += 1
    # print("step list in function: ", step_list)
    return step_list


if __name__ == "__main__":
    unittest.main()
