'''
Answer for Question 5 - The Training Again

Name: Jeslyn Joylie Bowman
SID: 530481526
unikey: jbow2146

'''

import q4

def main():
    q4.intro()
    q4.travel_to_camp()
    while True:
        result = q4.setup_trap(q4.trap)
        q4.hunt_result=q4.basic_hunt(result[0], result[1])
        hunt_status = q4.end(q4.hunt_result)
        if hunt_status:
            play_again = input('\nPress Enter to continue training and "no" to stop training: ')
            if play_again == "":
                continue
            if play_again == "no":
                break
        else:
            play_again = input('\nPress Enter to continue training and "no" to stop training: ')
            if play_again == "":
                continue
            if play_again == "no":
                break

if __name__ == '__main__':
    main()