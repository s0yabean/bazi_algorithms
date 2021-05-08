"""Create and bundle CSS and JS files."""
from flask_assets import Bundle, Environment


def compile_static_assets(app):
    """Configure static asset bundles."""
    assets = Environment(app)
    Environment.auto_build = True
    Environment.debug = False
    # Stylesheets Bundles
    tailwind_bundle = Bundle(
        "src/css/tailwind.css",
        output="dist/css/tailwind.css",
    )
    js_bundle = Bundle("src/js/main.js", filters="jsmin", output="dist/js/main.min.js")
    # Register assets
    assets.register("tailwind_bundle", tailwind_bundle)
    assets.register("js_all", js_bundle)
    # Build assets
    tailwind_bundle.build()
    js_bundle.build()
