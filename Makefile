PROJECT_NAME = service.pausespotify
RELEASE_VERSION = 0.1.0

release: clean
	mkdir -p $(PROJECT_NAME)
	cp -r addon.xml  default.py  icon.png  LICENSE  Makefile  pausespotify.py resources $(PROJECT_NAME)/
	zip -r "$(PROJECT_NAME)-$(RELEASE_VERSION).zip" $(PROJECT_NAME)

clean:
	-rm -rf *.zip
	-rm -rf *.pyo
	-rm -rf $(PROJECT_NAME)
