from .helper import Helper


class PeopleService:
    """
    Class Containing People related functions
    """

    people_url = "https://ghibliapi.herokuapp.com/people"

    people: list

    def get_people(self) -> list:
        """
        Get people through an api call
        :return: list
        @rtype: list
        """
        self.people = Helper.make_request(self.people_url)
        return self.people
