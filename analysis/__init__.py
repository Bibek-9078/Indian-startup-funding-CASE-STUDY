"""
The `analysis` package is a collection of modules for conducting various analyses
in the field of investment, startup evaluation, and overall performance assessment.

Modules:
- `investor`: This module provides functionality related to analyzing investor data,
including investor profiles, investment patterns, and performance metrics.
It contains classes and methods for retrieving and analyzing investor information.

- `startup`: This module offers functionality for evaluating startups,
including their financial health, growth potential, and market competitiveness.
It provides classes and methods for retrieving and analyzing startup data.

- `overall`: This module focuses on overall performance assessment, combining data
from investors and startups to provide a holistic analysis. It includes classes and
methods for conducting comprehensive evaluations and generating reports.

These modules can be used individually or in conjunction to perform in-depth analyses
and gain insights into investment trends, startup success factors, and overall market performance.

Usage:
To utilize the functionalities provided by this package, import the desired
modules into your Python script or interactive environment. For example:

from analysis.investor import Investor
from analysis.startup import Startup
from analysis.overall import Overall

# Use the classes and methods from the imported modules to perform analyses

Note: This package requires external dependencies such as data sources, APIs, or
datasets for retrieving relevant information.
Ensure that these dependencies are properly configured and accessible
before using the modules.

For detailed information about the classes, methods,
and their usage, refer to the individual module docstrings.
"""

from .investor import Investor
from .startup import Startup
from .overall import Overall
