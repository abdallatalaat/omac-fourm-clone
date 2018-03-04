class BaseStore:

    def __init__(self, data_provider, last_id):
        self.data_provider = data_provider
        self.last_id = last_id

    def get_all(self):
        return self.data_provider

    def add(self, entity):
        self.last_id += 1
        entity.id = self.last_id
        self.data_provider.append(entity)

    def entity_exists(self, entity):
        return entity is self.get_all()[entity.id]

    def delete(self, id):
        del self.data_provider[id - 1]

    def update(self, entity):
        self.data_provider[entity.id - 1] = entity

    def get_by_id(self, id):
        return self.data_provider[id - 1]


class MemberStore(BaseStore):
    members = []
    last_id = 0

    def __init__(self):
        super().__init__(MemberStore.members, MemberStore.last_id)


    def get_by_name(self, member_name):
        for member in MemberStore.members:
            if member.name == member_name:
                yield member

    def get_members_with_posts(self, all_posts):
        members = list(self.get_all())
        for member in members:
            for post in posts:
                if post.member_id == member.id:
                    member.posts.append(post)
        for member in members:
            yield member

    def get_top_two(self, all_posts):
        members = list(self.get_members_with_posts(all_posts))
        member_with_posts.sort(key = lambda member: len(member.posts), reverse=True)

        for i in range(2):
            yield members[i]

class PostStore(BaseStore):
    posts = []
    last_id = 0

    def __init__(self):
        super().__init__(PostStore.posts, PostStore.last_id)
