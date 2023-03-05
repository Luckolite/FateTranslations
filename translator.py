from discord import app_commands
from botutils import findall


class Translator(app_commands.Translator):
    translations = {}

    async def load(self):
        pass

    async def translate(self, string: app_commands.local_str, locale: discord.Locale, ctx: app_commands.TranslationContext):
        specials: list = await findall("\[.*]", string)
        stripped = str(string)
        for word in specials:
            stripped = stripped.replace(word, "%s")

        translation: str = self.translations[stripped]["the locale"]

        if stripped in self.translations:
            for i, word in enumerate(specials):
                translation.replace("%s", word, 1)

        return translation
