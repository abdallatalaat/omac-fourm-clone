class MemberStore:
    members = []
    m_id = 0

    def get_all(self):
        return members

    def add(self, member):
        MemberStore.m_id += 1
        member._id = MemberStore.m_id
        MemberStore.members.append(member)

    def entity_exists(self, member):
        return member is MemberStore.members[member._id]

    def delete(self, id):
        del MemberStore.members[id - 1]

    def get_by_id(self, id):
        return MemberStore.members[id - 1]

class PostStore:
    posts = []
    p_id = 0

    def get_all(self):
        return posts

    def add(self, post):
        PostStore.p_id += 1
        post._id = PostStore.p_id
        PostStore.posts.append(post)


    def get_by_id(self, id):
        return PostStore.posts[id - 1]
