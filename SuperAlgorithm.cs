#region Using declarations
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Input;
using System.Windows.Media;
using System.Xml.Serialization;
using NinjaTrader.Cbi;
using NinjaTrader.Gui;
using NinjaTrader.Gui.Chart;
using NinjaTrader.Gui.SuperDom;
using NinjaTrader.Data;
using NinjaTrader.NinjaScript;
using NinjaTrader.Core.FloatingPoint;
using NinjaTrader.NinjaScript.Indicators;
using NinjaTrader.NinjaScript.DrawingTools;
#endregion

namespace NinjaTrader.NinjaScript.Strategies
{
	public class SuperAlgorithm : Strategy
	{
		private SMA smaFast;
		private SMA smaSlow;

		protected override void OnStateChange()
		{
			if (State == State.SetDefaults)
			{
				Name		= "SuperAlgorithm";
				Fast		= 1;
				Slow		= 200;
				IsInstantiatedOnEachOptimizationIteration = false;
			}
			else if (State == State.DataLoaded)
			{
				smaFast = SMA(Fast);
				smaSlow = SMA(Slow);

				smaFast.Plots[0].Brush = Brushes.Goldenrod;
				smaSlow.Plots[0].Brush = Brushes.SeaGreen;

				AddChartIndicator(smaFast);
				AddChartIndicator(smaSlow);
			}
		}

		protected override void OnBarUpdate()
		{
			if (CurrentBar < BarsRequiredToTrade)
				return;

			if (CrossAbove(smaFast, smaSlow, 1))
				EnterLong(1);
			else if (CrossBelow(smaFast, smaSlow, 1))
				EnterShort(1);
		}

		#region Properties
		[Range(1, int.MaxValue), NinjaScriptProperty]
		[Display(ResourceType = typeof(Custom.Resource), Name = "Fast", GroupName = "NinjaScriptStrategyParameters", Order = 0)]
		public int Fast
		{ get; set; }

		[Range(1, int.MaxValue), NinjaScriptProperty]
		[Display(ResourceType = typeof(Custom.Resource), Name = "Slow", GroupName = "NinjaScriptStrategyParameters", Order = 1)]
		public int Slow
		{ get; set; }
		#endregion
	}
}
