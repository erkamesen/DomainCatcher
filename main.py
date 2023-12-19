from app.fetch import DomainCatcher


extensions = ["com", "net", "org"]
catcher = DomainCatcher(extensions)

catcher.run()