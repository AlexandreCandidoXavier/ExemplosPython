import numpy as np


def koppen_classification(precip, avgtemp, lat):
    """
    # codigo baseado em:
    # https://github.com/jgodwinWX/koppen/blob/master/koppen.py
    # https://www.nature.com/articles/sdata2018214
    # https://en.wikipedia.org/wiki/K%C3%B6ppen_climate_classification
    import koppen
    # dados das media mensais da precipitacao, temperatura e latitude do ligar
    precip = [96, 149, 110, 127, 120, 114.2, 114.2, 111.9, 111.8, 97.9, 101.6, 87.1]
    avgtemp = [25.5, 25.0, 24.1, 21.1, 17.6, 15.3, 14.8, 16.4, 17.3, 20.0, 22.1, 24.2]
    lat = -33.55
    koppen.koppen_classification(precip, avgtemp, lat)
    """
    precip = np.array(precip)
    avgtemp = np.array(avgtemp)
    total_prec = precip.sum()
    climate = ''

    # Group B (Arid and Semiarid)
    aridity = avgtemp.mean()*20
    if lat > 0:
        warm_precip = precip[3:9].sum()
        cool_precip = precip[0:3].sum() + precip[9:12].sum()
    else:
        warm_precip = precip[0:3].sum() + precip[9:12].sum()
        cool_precip = precip[3:9].sum()

    if warm_precip / total_prec >= 0.70:
        aridity = aridity + 280.0
    elif 0.30 <= warm_precip / total_prec < 0.70:
        aridity = aridity + 140.0
    else:
        aridity = aridity + 0.0

    # Arid Desert (BW)
    if total_prec / aridity < 0.50:
        # Hot Desert (BWh)
        if np.mean(avgtemp) > 18.0:
            climate = 'BWh'
        # Cold Desert (BWk)
        else:
            climate = 'BWk'
    # Semi-Arid/Steppe (BS)
    elif 0.50 <= total_prec / aridity < 1.00:
        # Hot Semi-Arid (BSh)
        if np.mean(avgtemp) > 18.0:
            climate = 'BSh'
        # Cold Semi-Arid (BSk)
        else:
            climate = 'BSk'

    if 'B' not in climate:
        # Group A (Tropical)
        if avgtemp.min() >= 18.0:
            # Tropical Rainforest
            if precip.min() >= 60.0:
                climate = 'Af'
            # Tropical Monsoon
            elif precip.min() < 60.0 and precip.sum() >= 25*(100 - precip.min()):  # (min(precip) / total_prec) > 0.04:
                climate = 'Am'
            else:
                if lat > 0:
                    # Tropical Savanna Dry summer
                    if 3 <= precip.argmin() <= 8:
                        climate = 'As'
                    # Tropical Savanna Dry Winter
                    else:
                        climate = 'Aw'
                else:
                    # Tropical Savanna Dry summer
                    if 3 <= precip.argmin() <= 8:
                        climate = 'Aw'
                    # Tropical Savanna Dry Winter
                    else:
                        climate = 'As'

        if 'A' not in climate:
            # Group C (Temperate)
            sortavgtemp = avgtemp
            sortavgtemp.sort()
            tempaboveten = (avgtemp > 10.0).sum()
            if lat > 0:
                coldwarmratio = precip[[0, 1, 11]].max() / precip[5:8].min()
                warmcoldratio = precip[5:8].sum() / precip[[0, 1, 11]].sum()
            else:
                coldwarmratio = precip[5:8].max() / precip[[0, 1, 11]].min()
                warmcoldratio = precip[[0, 1, 11]].sum() / precip[5:8].sum()

            if 0.0 <= avgtemp.min() <= 18.0 and avgtemp.max() >= 10.0:
                # Humid Subtropical (Cfa)
                if avgtemp.min() > 0.0 and avgtemp.max() > 22.0 and tempaboveten >= 4.0:
                    climate = 'Cfa'
                # Temperate Oceanic (Cfb)
                elif avgtemp.min() > 0.0 and avgtemp.max() < 22.0 and tempaboveten >= 4.0:
                    climate = 'Cfb'
                # Subpolar Oceanic (Cfc)
                elif avgtemp.min() > 0.0 and 1 <= tempaboveten <= 3:
                    climate = 'Cfc'

                # Monsoon-influenced humid subtropical (Cwa)
                if avgtemp.min() > 0.0 and avgtemp.max() > 22.0 and tempaboveten >= 4 and warmcoldratio > 10.0:
                    climate = 'Cwa'
                # Subtropical Highland/Temperate Oceanic with Dry Winter (Cwb)
                elif avgtemp.min() > 0.0 and avgtemp.max() < 22.0 and tempaboveten >= 4 and warmcoldratio > 10.0:
                    climate = 'Cwb'
                # Cold Subtropical Highland/Subpolar Oceanic with Dry Winter (Cwc)
                elif avgtemp.min() > 0.0 and tempaboveten >= 1 and tempaboveten <= 3 and warmcoldratio > 10.0:
                    climate = 'Cwc'

                # Hot np.summer Mediterranean (Csa)
                if lat > 0:
                    prec_min_month_summer = precip[5:8].min()
                else:
                    prec_min_month_summer = precip[[0, 1, 11]].min()

                if avgtemp.min() > 0.0 and avgtemp.max() > 22.0 and tempaboveten >= 4 and \
                        coldwarmratio >= 3.0 and prec_min_month_summer < 30.0:
                    climate = 'Csa'
                # Warm np.summer Mediterranean (Csb)
                elif avgtemp.min() > 0.0 and avgtemp.max() < 22.0 and tempaboveten >= 4 and \
                        coldwarmratio >= 3.0 and prec_min_month_summer < 30.0:
                    climate = 'Csb'
                # Cool np.summer Mediterranean (Csc)
                elif avgtemp.min() > 0.0 and tempaboveten >= 1 and tempaboveten <= 3 and \
                        coldwarmratio >= 3.0 and prec_min_month_summer < 30.0:
                    climate = 'Csc'

                if 'C' not in climate:
                    # Group D (Continental)
                    if avgtemp.min() < 0.0 and avgtemp.max() > 10.0:
                        # Hot np.summer humid continental (Dfa)
                        if avgtemp.min() > 22.0 and tempaboveten >= 4:
                            climate = 'Dfa'
                        # Warm np.summer humid continental (Dfb)
                        elif avgtemp.max() < 22.0 and tempaboveten >= 4:
                            climate = 'Dfb'
                        # Subarctic (Dfc)
                        elif tempaboveten >= 1 and tempaboveten <= 3:
                            climate = 'Dfc'
                        # Extremely cold subarctic (Dfd)
                        elif avgtemp.min() < -38.0 and tempaboveten >= 1 and tempaboveten <= 3:
                            climate = 'Dfd'

                        # Monsoon-influenced hot humid continental (Dwa)
                        if avgtemp.max() > 22.0 and tempaboveten >= 4 and warmcoldratio >= 10:
                            climate = 'Dwa'
                        # Monsoon-influenced warm humid continental (Dwb)
                        elif avgtemp.max() < 22.0 and tempaboveten >= 4 and warmcoldratio >= 10:
                            climate = 'Dwb'
                        # Monsoon-influenced subarctic (Dwc)
                        elif tempaboveten >= 1 and tempaboveten <= 3 and warmcoldratio >= 10:
                            climate = 'Dwc'
                        # Monsoon-influenced extremely cold subarctic (Dwd)
                        elif avgtemp.min() < -38.0 and tempaboveten >= 1 and tempaboveten <= 3 and warmcoldratio >= 10:
                            climate = 'Dwd'

                        # Hot, dry continental (Dsa)
                        if avgtemp.max() > 22.0 and tempaboveten >= 4 and coldwarmratio >= 3 and min(precip[5:8]) < 30.0:
                            climate = 'Dsa'
                        # Warm, dry continental (Dsb)
                        elif avgtemp.max() < 22.0 and tempaboveten >= 4 and coldwarmratio >= 3 and min(precip[5:8]) < 30.0:
                            climate = 'Dsb'
                        # Dry, subarctic (Dsc)
                        elif tempaboveten >= 1 and tempaboveten <= 3 and coldwarmratio >= 1 and coldwarmratio >= 3 and \
                                precip[5:8].min() < 30.0:
                            climate = 'Dsc'
                        # Extremely cold, dry subarctic (Dsd)
                        elif avgtemp.min() < -38.0 and tempaboveten >= 1 and tempaboveten <= 3 and coldwarmratio >= 3 and \
                                precip[5:8].min() < 30.0:
                            climate = 'Dsd'

                        if 'D' not in climate:
                            # Group E (Polar and alpine)
                            if avgtemp.max() < 10.0:
                                # Tundra (ET)
                                if avgtemp.max() > 0.0:
                                    climate = 'ET'
                                # Ice cap (EF)
                                else:
                                    climate = 'EF'
    return climate
