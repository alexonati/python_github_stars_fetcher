class GitHubRepo:
     
    def __init__(self, name, language, num_stars):
         self.name = name
         self.language = language
         self.num_stars = num_stars
    
    def __str__(self):
        return f'-> {name} is a {language} repo with {stars}'