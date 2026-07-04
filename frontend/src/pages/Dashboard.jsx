import Hero from "../components/dashboard/Hero";
import StatsGrid from "../components/dashboard/StatsGrid";
import BusinessHealth from "../components/dashboard/BusinessHealth";
import ActivityTimeline from "../components/dashboard/ActivityTimeline";
import QuickActions from "../components/dashboard/QuickActions";
import RecentApprovals from "../components/dashboard/RecentApprovals";
import RevenueChart from "../components/dashboard/RevenueChart";

import useDashboard from "../hooks/useDashboard";

export default function Dashboard() {

  const { loading, data } = useDashboard();

  if (loading) {
    return (
      <div className="h-[80vh] flex items-center justify-center">

        <div className="text-center">

          <div className="h-20 w-20 rounded-full border-4 border-violet-500 border-t-transparent animate-spin mx-auto"></div>

          <h2 className="mt-8 text-2xl font-bold">
            AI COO is analysing your business...
          </h2>

        </div>

      </div>
    );
  }

  return (
    <div className="space-y-8">

      <Hero />

      <StatsGrid data={data} />

      <div className="grid xl:grid-cols-3 gap-6">

        <BusinessHealth />

        <QuickActions />

        <RecentApprovals />

      </div>

      <div className="grid xl:grid-cols-2 gap-6">

        <RevenueChart />

        <ActivityTimeline />

      </div>

    </div>
  );
}