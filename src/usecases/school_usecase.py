class CreateSchool:
    def __init__(self, school_repo):
        self.school_repo = school_repo

    def execute(self, school_data):
        school_id = self.school_repo.create(school_data)

        return {"id": school_id}
