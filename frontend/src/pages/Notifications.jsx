import useNotifications from "../hooks/useNotifications";

export default function Notifications() {

  const { notifications, loading } = useNotifications();

  if (loading)
    return <h2>Loading...</h2>;

  return (

    <div>

      <h1 className="text-4xl font-bold mb-8">

        Notifications

      </h1>

      <div className="space-y-5">

        {notifications.map((item, index) => (

          <div
            key={index}
            className="rounded-2xl bg-white/5 border border-white/10 p-6"
          >

            <h2 className="text-xl font-semibold">

              {item.title}

            </h2>

            <p className="text-gray-400 mt-2">

              {item.message}

            </p>

          </div>

        ))}

      </div>

    </div>

  );

}