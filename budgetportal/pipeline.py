from __future__ import absolute_import

import codecs

import scss
from django.conf import settings
from pipeline.compilers import SubProcessCompiler
from pipeline.storage import PipelineMixin
from whitenoise.storage import CompressedManifestStaticFilesStorage


class CompressedManifestPipelineStorage(
    PipelineMixin, CompressedManifestStaticFilesStorage
):
    pass


class PyScssCompiler(SubProcessCompiler):
    output_extension = "css"

    def match_file(self, filename):
        return filename.endswith(".scss")

    def compile_file(self, infile, outfile, outdated=False, force=False):
        if not outdated and not force:
            return

        result = scss.compiler.compile_file(
            infile, search_path=settings.PYSCSS_LOAD_PATHS
        )

        with codecs.open(outfile, "w", encoding="utf-8") as f:
            f.write(result)
