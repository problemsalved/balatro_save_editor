import os

from balatro_save_file import BalatroSaveFile


class BalatroSaveEditor(object):
    def __init__(self, save_file_path):
        self.balatro_save_file = BalatroSaveFile(save_file_path)

    def edit_money(self, new_value):
        # Sets the amount of money you have
        self.balatro_save_file['GAME']['dollars'] = str(new_value)

    def edit_chips(self):
        # Searches for the current blind's chip target and sets your current chip count to just under it
        try:
            target = int(self.balatro_save_file['BLIND']['chips'].structs[0])
        except ValueError:
            target = int(float(self.balatro_save_file['BLIND']['chips'].structs[0]))
        self.balatro_save_file['GAME']['chips'] = str(target - 1)
        self.balatro_save_file['GAME']['chips_text'] = f'{target - 1:,}'

    def edit_multipliers(self, new_mult=10000):
        # Changes the multiplier for each hand type
        for hand in self.balatro_save_file['GAME']['hands']:
            hand['mult'] = str(new_mult)

    def edit_card_limits(self):
        # Change joker limit
        self.balatro_save_file['cardAreas']['jokers']['config']['card_limit'] = str(20)
        self.balatro_save_file['cardAreas']['jokers']['config']['temp_limit'] = str(20)
        # Change consumable (tarot cards) limit
        self.balatro_save_file['cardAreas']['consumeables']['config']['card_limit'] = str(10)
        self.balatro_save_file['cardAreas']['consumeables']['config']['temp_limit'] = str(10)

    def edit_card_abilities(self):
        # This removes the 'eternal' attribute from all cards in your deck
        for joker in self.balatro_save_file['cardAreas']['jokers']['cards']:
            if 'eternal' in joker['ability']:
                joker['ability']['eternal'] = 'false'


def main():
    balatro_save_editor = BalatroSaveEditor(os.path.join(os.getenv('APPDATA'), 'Balatro\\1\\save.jkr'))
    balatro_save_editor.edit_money(new_value=19999)
    balatro_save_editor.edit_chips()
    balatro_save_editor.edit_multipliers()
    balatro_save_editor.edit_card_abilities()
    balatro_save_editor.edit_card_limits()
    balatro_save_editor.balatro_save_file.write(dry_run=False)


if __name__ == '__main__':
    main()
