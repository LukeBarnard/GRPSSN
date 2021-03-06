import os


class SSN_Data:
    """
    Blank class for managing SSN data.
    Can assign named variables to this class to avoid global class variables
    """
    pass


class SSN_GRP_Config:
    """
    Class to store static config variables
    """

    # MULTIPROCESSING
    # 1 --> do not use any parallel processing.
    # -1 -->  use all cores on machine.
    # Other --> defines number of cores to use
    PROCESSES = 1

    # SCATTER PLOT AND R2 OPTIONS
    # "true" --> Use sqrt(GN + 1)
    # "False" --> Use GN
    SQRT_2DHIS = False

    # OVERWRITING AND SKIPPING PLOTS
    # Setting both flags to false will recreate and overwrite all plots for all observers
    # Overwrite plots already present
    # Even when false, still have to process each observer
    # Safer than the SKIP_OBSERVERS_WITH_PLOTS flag
    SKIP_PRESENT_PLOTS = False
    # Ignore any observer that has any plots with current flags in its output folder
    # Skips processing observer data making the process much faster
    # However, if a plot that should have been made previously is missing it will not be made when this flag is enabled
    # More dangerous than SKIP_PRESENT_PLOTS, but good when confident that existing observers were completely processed
    SKIP_OBSERVERS_WITH_PLOTS = False

    # Plotting config variables
    PLOT_SN_GRP = True
    PLOT_SN_AL = True
    PLOT_OPTIMAL_THRESH = True
    PLOT_ACTIVE_OBSERVED = True
    PLOT_DIST_THRESH_MI = True
    PLOT_INTERVAL_SCATTER = True
    PLOT_INTERVAL_DISTRIBUTION = True
    PLOT_MIN_EMD = True
    PLOT_SIM_FIT = True
    PLOT_DIST_THRESH = True
    PLOT_SINGLE_THRESH_SCATTER = True
    PLOT_SINGLE_THRESH_DIS = True
    PLOT_MULTI_THRESH_SCATTER = True
    PLOT_SMOOTHED_SERIES = True

    # Suppress numpy warnings for cleaner console output
    SUPPRESS_NP_WARNINGS = False

    @staticmethod
    def get_file_prepend():
        """
        :param num_type: GRP parameter set in config
        :param den_type: month length parameter set in config
        :return: prepend for plots depending on GRP and month length
        """

        prepend = "GRP_"

        return prepend

    @staticmethod
    def get_file_output_string(number, title, ssn_data):
        """
        :param number: Plot type identifier
        :param title: Plot title
        :param ssn_data: SSN_Data object storing metadata
        :param num_type: GRP parameter set in config
        :param den_type: month length parameter set in config
        :return: Path
        """
        return os.path.join(ssn_data.output_path,
                            "{}_{}".format(ssn_data.CalObs, ssn_data.NamObs),
                            "{}_{}_{}_{}_{}.png".format(number,
                                                        SSN_GRP_Config.get_file_prepend(),
                                                        ssn_data.CalObs,
                                                        ssn_data.NamObs,
                                                        title))